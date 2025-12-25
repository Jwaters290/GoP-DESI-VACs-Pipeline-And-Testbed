# GoP–Decoherence–Driven Curvature

This repository provides the **reference implementation** of the Gravity of Probability (GoP)
probabilistic curvature framework and its associated prediction pipelines.

It implements the **probabilistic stress–energy contribution**:

T_prob(μν)

arising from quantum decoherence and entanglement, and provides tools for
galaxy dynamics, gravitational lensing, and large-scale structure tests.

## Included Components

- Canonical decoherence kernel Γ(E)
- Global GoP constants (fixed, pre-registered)
- Probabilistic stress–energy tensor tools
- Warm-core and cosmic void predictions
- Rotation curve and lensing utilities
- DESI / Euclid large-scale structure test scripts

This is the **official codebase** used for GoP predictions in cosmology and LSS analyses.

---

# DESI Warm-Core Prediction Script

### File: `gop_warm_core_desipipeline.py` (repo root)

This script implements the GoP warm-core prediction using the fixed July 2025 parameter set:

- kappaA = 1.5e-15  
- E0_erg = 1e12  
- f_ent = 0.20  
- A_CP = 0.0245  

It computes:

- Baryonic density profile ρ_b(r)
- Probabilistic density contribution ρ_prob(r)
- Effective density ρ_eff(r)
- Inner density slope (cusp vs. core)
- Warm-core enhancement factor
- Diagnostic plots compatible with DESI stacked void analyses

Run the script:

```bash
python gop_warm_core_desipipeline.py
```
Expected (pre-registered):

- Inner slope transitions from cusp-like (≈ −1) to core-like (≈ 0)
- Warm central void structure
- Radial profile matching DESI DR2 VAC predictions

----


---

## Vacuum Stability & Λ_eff Consistency

A **companion repository** numerically verifies the stability of the effective vacuum energy
produced by the GoP decoherence kernel:

- https://github.com/Jwaters290/GoP-vs-Lambda-Vacuum-Constant

This test demonstrates that the canonical kernel

Γ(E) = κA · E · exp(1 − E / E₀)

**naturally saturates**, producing a stable effective cosmological constant Λ_eff under
cosmological conditions.

### Key Results

- No overproduction of vacuum energy
- Rapid convergence to a constant Λ_eff
- Stability under extreme energy distributions
- Compatibility with late-time acceleration
- No fine-tuning required

Consistency is demonstrated relative to:

- Planck CMB ΛCDM parameters
- DESI BAO expansion history
- Type Ia supernova luminosity distances

This validates GoP as a **dark-matter-free curvature model that remains cosmologically viable**.

---

## GoP Predictions for DESI DR2 (Pre-Registered)

All predictions below are based on a **single fixed global parameter set** (no tuning):

- Warm-core cosmic void temperature imprint: ΔT ≈ 8–12 μK
- Void redshift peak: z ≈ 0.55
- Suppressed clustering amplitude: S₈ ≈ 0.76–0.79
- Dipole amplification factor: 1.2×–1.5×
- BAO peak smoothing / broadening
- H(z) crossover near z ≈ 0.45–0.55
- Tracer independence (BGS, LRG, ELG, QSO voids)

---

## Citations

Jordan Waters  
**“The Gravity of Probability: Replicating Dark Matter Effects Through Quantum Decoherence Curvature”**  
DOI: 10.6084/m9.figshare.29815934  
https://figshare.com/articles/thesis/The_Gravity_of_Probability/29815934  

Jordan Waters  
**“DESI DR2 VACs Predictions”**  
DOI: 10.6084/m9.figshare.30593876  
https://figshare.com/articles/preprint/DESI_DR2_VACs_Predictions/30593876  

Jordan Waters  
**“Foundations of the Gravity of Probability”**  
DOI: 10.6084/m9.figshare.30662603  
https://figshare.com/articles/preprint/Foundations_of_the_Gravity_of_Probability/30662603  

ORCID  
https://orcid.org/0009-0009-0793-8089  

Figshare Profile  
https://figshare.com/authors/Jordan_Waters/21620558  

---

## Background: Probabilistic Curvature

The GoP framework modifies the total stress–energy tensor:

T_total(μν) = T_classical(μν) + T_prob(μν)

Where:

- T_classical represents standard matter and radiation
- T_prob arises from decoherence-weighted quantum probability curvature

Canonical form:

T_prob(μν) ∝ Γ(E) · ρ_Ψ

Where:

- Γ(E) is the GoP decoherence kernel (includes κA by convention)
- ρ_Ψ is the entanglement-weighted baryonic density

All global parameters are **fixed prior to DESI DR2 analysis**.

---

## Installation

```bash
git clone https://github.com/Jwaters290/GoP-Probabilistic-Curvature.git
cd GoP-Probabilistic-Curvature
pip install -r requirements.txt
```

---

## Quickstart (Core Prediction)

Template-mode run (shows the warm-core shape and prints diagnostics):

```bash
python gop_warm_core_desipipeline.py --mode normalized --debug
```

Production-mode run (dimensionally consistent; requires physical density units and a chosen coherence scale):
```
bash
Copy code
python gop_warm_core_desipipeline.py --mode physical --Lcoh-cm 1e18 --debug
```
---

# VAC Phasing & Falsifiability Roadmap

Phase I — Lyman-Alpha / LSS Power Spectrum (2026)

Prediction:
ΔP/P ≈ 0.02–0.04 at k ≈ 0.1 h/Mpc

Run:
```bash
python scripts/gop_lss_earlytest.py --pk-file desi_pk.dat
```
Phase II — Void Stacking (Primary Test)

DESI stacked voids should show:

- warm central region
- redshift peak at z ≈ 0.55
- curvature residual matching GoP predictions

Run:
```bash
python gop_warm_core_desipipeline.py
```

---

## Developer Note: Switching to Full GoP P(k)
The default LSS test uses a Gaussian modifier for early testing.
To switch to the full GoP cosmology:
```
from gop_core.gop_cosmology import compute_pk_gop

def gop_predict_modifier(k_array, cosmo=None):
    return compute_pk_gop(k_array, **(cosmo or {}))

```
This upgrades the script to the full GoP cosmology.


---

# Keywords
gravity-of-probability, decoherence, probabilistic-curvature, alternative-gravity,
S8-tension, DESI-DR2, warm-void-core, void-redshift-peak-0.55, S8-0.76-0.79,
dipole-amplification, BAO-smoothing, DESI, DESI-DR1, Lyman-alpha, LyA-forest,
large-scale-structure, LSS, Pk-tilt, matter-power-spectrum, BAO-smearing,
cosmic-voids, void-stacking, SPARC-rotation-curves, falsifiable-gravity-model,
pre-registered-predictions, DESI-void-test, ACP-CP-violation

---

