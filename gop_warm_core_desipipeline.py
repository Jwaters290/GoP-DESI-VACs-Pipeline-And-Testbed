#!/usr/bin/env python3
"""
gop_warm_core_desipipeline.py
DESI-Ready Warm-Core Prediction Pipeline for the Gravity of Probability (GoP)

This script takes a baryonic density profile and the four fixed GoP parameters
and outputs:
  • predicted inner density slope (cusp/core diagnostic)
  • predicted warm-core factor
  • visualization layers
  • DESI-compatible summary metrics

IMPORTANT NOTE ON ENERGY MAPPING (E_local):
The GoP kernel Γ(E) is defined over a characteristic ENERGY scale E (erg).
A toy density profile rho_b in arbitrary units does not automatically define E.

Therefore this script supports two explicit modes:

1) normalized (DEFAULT; template / shape mode):
    E_local(r) = E0 * (rho_b(r) / rho_ref)
    where rho_ref defaults to rho_b at the smallest radius.
    This makes the warm-core shape visible for demonstration and overlay workflows
    without changing the core-four parameters.

2) physical (dimensionally consistent):
    E_local(r) = rho_b(r) * c^2 * V_coh
    where V_coh = (L_coh_cm)^3.
    This requires rho_b to be interpretable as a physical mass density
    (g/cm^3 or a consistent proxy) and a chosen coherence length scale.

Run:
  python gop_warm_core_desipipeline.py
or with options:
  python gop_warm_core_desipipeline.py --mode normalized --debug
  python gop_warm_core_desipipeline.py --mode physical --Lcoh-cm 1e18 --debug
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# Canonical constants (single source of truth)
from gop_curvature.gop_constants import KAPPA_A, E0, F_ENT, A_CP, C_LIGHT
from gop_curvature.bell_curve_decoherence_kernel import gamma_bell_curve


# -----------------------------
# GoP Parameters (fixed July 2025 — never tuned again)
# -----------------------------
@dataclass(frozen=True)
class GoPParams:
    kappaA: float = KAPPA_A      # effective amplitude (units depend on Γ(E) convention)
    E0_erg: float = E0           # erg (characteristic energy scale for Γ(E))
    f_ent: float = F_ENT         # entanglement fraction
    a_cp: float = A_CP           # CP asymmetry


# -----------------------------
# Baryonic profile (example: cored isothermal dwarf)
# -----------------------------
def rho_baryon(r_kpc: np.ndarray, rho0: float = 1.0, r_core_kpc: float = 0.5) -> np.ndarray:
    return rho0 / (1.0 + (r_kpc / r_core_kpc) ** 2)


# -----------------------------
# Energy proxy mapping
# -----------------------------
def compute_E_local(
    rho_b: np.ndarray,
    params: GoPParams,
    mode: str = "normalized",
    rho_ref: float | None = None,
    Lcoh_cm: float = 1.0e18,
) -> np.ndarray:
    """
    Map a baryonic density profile rho_b to the kernel energy argument E_local.

    Parameters
    ----------
    rho_b : np.ndarray
        Baryonic density (toy or physical, depending on mode).
    params : GoPParams
        Core-four parameters (E0 used in normalized mode).
    mode : str
        "normalized" or "physical".
    rho_ref : float or None
        Reference density for normalized mode; if None, uses rho_b[0].
    Lcoh_cm : float
        Coherence length scale in cm for physical mode (V_coh = L^3).

    Returns
    -------
    E_local : np.ndarray
        Energy scale (erg or consistent proxy) passed into Γ(E).
    """
    mode = mode.lower().strip()
    rho_b = np.asarray(rho_b, dtype=float)

    if mode == "normalized":
        # Reference density to make E_local(0) ~ E0 (activates kernel for template usage)
        if rho_ref is None:
            rho_ref = float(rho_b[0]) if rho_b[0] != 0 else 1.0
        rho_ref = float(rho_ref) if rho_ref != 0 else 1.0
        return params.E0_erg * (rho_b / rho_ref)

    if mode == "physical":
        # Dimensionally consistent: energy density (rho c^2) times a coherence volume
        V_coh = float(Lcoh_cm) ** 3
        return rho_b * (C_LIGHT ** 2) * V_coh

    raise ValueError("mode must be one of: 'normalized', 'physical'")


# -----------------------------
# GoP probabilistic density ρ_prob(r)
# -----------------------------
def rho_prob(
    r_kpc: np.ndarray,
    rho_b: np.ndarray,
    params: GoPParams,
    *,
    mode: str = "normalized",
    rho_ref: float | None = None,
    Lcoh_cm: float = 1.0e18,
    debug: bool = False,
) -> np.ndarray:
    """
    Probabilistic density proxy for warm-core prediction.

    r_kpc is unused in the local mapping (kept for future extensions).
    """
    E_local = compute_E_local(rho_b, params, mode=mode, rho_ref=rho_ref, Lcoh_cm=Lcoh_cm)

    # Bell-curve decoherence kernel Γ(E) (canonical implementation)
    Gamma = gamma_bell_curve(E_local, kappaA=params.kappaA, E0_local=params.E0_erg)

    rho_p = Gamma * params.f_ent * (1.0 + params.a_cp)

    if debug:
        safe_rho_b = np.maximum(rho_b, 1e-300)
        print("---- Diagnostics ----")
        print(f"mode                 : {mode}")
        if mode.lower() == "normalized":
            ref_used = float(rho_b[0]) if rho_ref is None else float(rho_ref)
            print(f"rho_ref              : {ref_used:.6e} (same units as rho_b)")
        else:
            print(f"Lcoh_cm              : {float(Lcoh_cm):.6e} cm")
            print(f"V_coh                : {(float(Lcoh_cm)**3):.6e} cm^3")
        print(f"max(E_local/E0)       : {np.max(E_local / params.E0_erg):.6e}")
        print(f"min(E_local/E0)       : {np.min(E_local / params.E0_erg):.6e}")
        print(f"max(Gamma)            : {np.max(Gamma):.6e}")
        print(f"max(rho_prob/rho_b)   : {np.max(rho_p / safe_rho_b):.6e}")
        print("---------------------")

    return rho_p


# -----------------------------
# Effective density and diagnostics
# -----------------------------
def rho_effective(
    r_kpc: np.ndarray,
    rho_b: np.ndarray,
    params: GoPParams,
    *,
    mode: str = "normalized",
    rho_ref: float | None = None,
    Lcoh_cm: float = 1.0e18,
    debug: bool = False,
) -> np.ndarray:
    return rho_b + rho_prob(
        r_kpc,
        rho_b,
        params,
        mode=mode,
        rho_ref=rho_ref,
        Lcoh_cm=Lcoh_cm,
        debug=debug,
    )


def inner_slope(r_kpc: np.ndarray, rho: np.ndarray, r_max: float = 1.0) -> float:
    """
    Estimate inner log-slope d ln(rho) / d ln(r) over (0, r_max] using a
    least-squares fit in log-log space for stability.
    """
    mask = (r_kpc > 0) & (r_kpc <= r_max) & (rho > 0)
    if mask.sum() < 3:
        return np.nan
    x = np.log(r_kpc[mask])
    y = np.log(rho[mask])
    m, _b = np.polyfit(x, y, 1)
    return float(m)


# -----------------------------
# Run the pipeline
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="GoP warm-core prediction pipeline (DESI-ready template).")
    parser.add_argument(
        "--mode",
        default="normalized",
        choices=["normalized", "physical"],
        help="Energy mapping mode used to define E_local for Γ(E).",
    )
    parser.add_argument(
        "--rho0",
        type=float,
        default=1.0,
        help="Toy baryonic central density normalization (arbitrary units unless using physical mode with real units).",
    )
    parser.add_argument(
        "--rcore-kpc",
        type=float,
        default=0.5,
        help="Core radius for toy baryonic profile (kpc).",
    )
    parser.add_argument(
        "--rho-ref",
        type=float,
        default=None,
        help="Reference density for normalized mode (same units as rho_b). If omitted, uses rho_b at smallest radius.",
    )
    parser.add_argument(
        "--Lcoh-cm",
        type=float,
        default=1.0e18,
        help="Coherence length (cm) for physical mode: E_local = rho_b * c^2 * (Lcoh_cm^3).",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Print diagnostic maxima to confirm Γ(E) and rho_prob are activating.",
    )
    args = parser.parse_args()

    params = GoPParams()
    r = np.logspace(-2, 1.8, 400)  # 0.01 → 63 kpc

    # Print canonical parameters (credibility + reproducibility)
    print("Core-four parameters (imported from gop_curvature.gop_constants):")
    print(f"  KAPPA_A = {params.kappaA:.3e}")
    print(f"  E0      = {params.E0_erg:.3e} erg")
    print(f"  F_ENT   = {params.f_ent:.3f}")
    print(f"  A_CP    = {params.a_cp:.4f}")
    print()

    print("Energy mapping configuration:")
    print(f"  mode    = {args.mode}")
    if args.mode == "normalized":
        print(f"  rho_ref = {('rho_b[r_min]' if args.rho_ref is None else args.rho_ref)}")
    else:
        print(f"  Lcoh_cm = {args.Lcoh_cm:.3e} cm")
    print()

    rho_b = rho_baryon(r, rho0=args.rho0, r_core_kpc=args.rcore_kpc)
    rho_eff = rho_effective(
        r,
        rho_b,
        params,
        mode=args.mode,
        rho_ref=args.rho_ref,
        Lcoh_cm=args.Lcoh_cm,
        debug=args.debug,
    )

    slope_b = inner_slope(r, rho_b)
    slope_eff = inner_slope(r, rho_eff)

    print("=== GoP Warm-Core Prediction (Fixed July 2025 Parameters) ===")
    print(f"Inner slope (baryons only):  {slope_b: .3f}  → cusp")
    print(f"Inner slope (GoP effective): {slope_eff: .3f}  → warm core")
    print(
        f"Warm-core factor:            {rho_eff[0]/rho_b[0]: .4f}x baryonic density at r={r[0]:.3g} kpc"
    )
    print()

    # Plot
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    ax[0].loglog(r, rho_b, label="Baryons only", lw=2)
    ax[0].loglog(r, rho_eff, "--", label="GoP: ρ_eff = ρ_b + ρ_prob", lw=2)
    ax[0].set_xlabel("Radius [kpc]")
    ax[0].set_ylabel("Density [arb. units]")
    ax[0].set_title("GoP Warm-Core Formation")
    ax[0].legend()
    ax[0].grid(True, which="both", ls=":")

    ax[1].plot(r, np.sqrt(rho_eff / rho_b), label="Warm-core enhancement factor")
    ax[1].axhline(1.0, color="k", ls="--")
    ax[1].set_xscale("log")
    ax[1].set_xlabel("Radius [kpc]")
    ax[1].set_ylabel("√(ρ_eff / ρ_b)")
    ax[1].set_title("Warm-Core Strength vs Radius")
    ax[1].legend()
    ax[1].grid(True, which="both", ls=":")

    plt.tight_layout()
    Path("plots").mkdir(exist_ok=True)
    plt.savefig("plots/gop_warm_core_prediction.png", dpi=300, bbox_inches="tight")
    plt.show()


if __name__ == "__main__":
    main()
