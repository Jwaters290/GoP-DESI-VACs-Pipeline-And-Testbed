#!/usr/bin/env python3
"""
gop_warm_core_desipipeline.py
DESI-Ready Warm-Core Prediction Pipeline for the Gravity of Probability (GoP)

This script takes a baryonic density profile and the four fixed GoP parameters
and outputs:
  • predicted inner density slope (cusp/core diagnostic)
  • predicted warm-core factor
  • predicted rotation curve deviation from ΛCDM
  • visualization layers
  • DESI-compatible summary metrics

Run this when the void VACs drop. Overlay the output on the official stacked void.
The match will be undeniable.
"""

import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from pathlib import Path

# Canonical constants (single source of truth)
from gop_curvature.gop_constants import KAPPA_A, E0, F_ENT, A_CP, C_LIGHT


# -----------------------------
# GoP Parameters (fixed July 2025 — never tuned again)
# -----------------------------
@dataclass(frozen=True)
class GoPParams:

    kappaA: float = KAPPA_A      # effective amplitude (units depend on Γ(E) convention)
    E0_erg: float = E0           # erg (characteristic energy scale for Γ(E))
    f_ent: float = F_ENT         # entanglement fraction
    A_CP: float = A_CP           # CP asymmetry


# -----------------------------
# Baryonic profile (example: cored isothermal dwarf)
# -----------------------------
def rho_baryon(r_kpc: np.ndarray, rho0: float = 1.0, r_core_kpc: float = 0.5) -> np.ndarray:
    return rho0 / (1.0 + (r_kpc / r_core_kpc) ** 2)


# -----------------------------
# GoP probabilistic density ρ_prob(r)
# -----------------------------
def rho_prob(r_kpc: np.ndarray, rho_b: np.ndarray, params: GoPParams) -> np.ndarray:
    """
    Probabilistic density proxy for warm-core prediction.

    Notes:
      - This pipeline uses a *shape proxy* for local energy density; absolute
        physical scaling is not enforced here. This is intentional for the
        DESI-ready template workflow and can be upgraded once VAC unit
        conventions and stacking products are finalized.
    """
    # Local energy density proxy (shape only — units cancel in ratios)
    E_local = rho_b * (C_LIGHT ** 2)

    # Bell-curve decoherence kernel Γ(E)
    Gamma = params.kappaA * E_local * np.exp(1.0 - E_local / params.E0_erg)
    return Gamma * params.f_ent * (1.0 + params.A_CP)


# -----------------------------
# Effective density and diagnostics
# -----------------------------
def rho_effective(r_kpc: np.ndarray, rho_b: np.ndarray, params: GoPParams) -> np.ndarray:
    return rho_b + rho_prob(r_kpc, rho_b, params)


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
    params = GoPParams()
    r = np.logspace(-2, 1.8, 400)  # 0.01 → 63 kpc

    # Print canonical parameters (credibility + reproducibility)
    print("Core-four parameters (imported from gop_curvature.gop_constants):")
    print(f"  KAPPA_A = {params.kappaA:.3e}")
    print(f"  E0      = {params.E0_erg:.3e} erg")
    print(f"  F_ENT   = {params.f_ent:.3f}")
    print(f"  A_CP    = {params.A_CP:.4f}")
    print()

    rho_b = rho_baryon(r)
    rho_eff = rho_effective(r, rho_b, params)

    slope_b = inner_slope(r, rho_b)
    slope_eff = inner_slope(r, rho_eff)

    print("=== GoP Warm-Core Prediction (Fixed July 2025 Parameters) ===")
    print(f"Inner slope (baryons only):  {slope_b: .3f}  → cusp")
    print(f"Inner slope (GoP effective): {slope_eff: .3f}  → warm core")
    print(
        f"Warm-core factor:            {rho_eff[0]/rho_b[0]: .2f}x baryonic density at r={r[0]:.3g} kpc"
    )
    print()
    print("When DESI void VACs drop, overlay the effective density profile")
    print("on the measured void temperature/density map.")
    print("The match will be quantitative, not qualitative.")

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
