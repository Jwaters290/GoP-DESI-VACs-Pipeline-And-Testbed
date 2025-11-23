# Gravity of Probability (GoP)
**Keywords:** gravity-of-probability, decoherence, probabilistic-curvature, alternative-gravity, S8-tension, DESI DR2, warm void core prediction, mid-z void peak z=0.55, S₈ = 0.76–0.79 prediction, dipole amplification (1.2×–1.5×) prediction, BAO smoothing prediction

# GoP-Probabilistic-Curvature

Reference implementation of the Gravity of Probability (GoP) probabilistic curvature term Tᵤₙᵤᵖʳᵒᵇ. Includes decoherence kernel Γ(E), global GoP constants, and Tᵐᵤₙᵤ^{prob} calculator for use in cosmology, lensing, and galaxy modeling.

# Gravity of Probability (GoP) — Probabilistic Curvature Kernel


This repository contains the official Python implementation of the GoP probabilistic curvature tensor Tᵘₙᵤᵖʳᵒᵇ, 
including the decoherence kernel Γ(E), global GoP constants, and tools for computing rotation curves, 
gravitational lensing, void thermodynamics, and large-scale structure predictions. This is the primary 
codebase used for GoP predictions in DESI, Euclid, CMB, and lensing analyses.

### GoP Predictions (DESI DR2 VACs)

1. Warm-core cosmic void temperature imprint  
2. Void redshift peak at z≈0.55  
3. S₈ suppressed to 0.76–0.79  
4. Cosmic dipole amplification factor 1.2×–1.5×  
5. BAO peak smoothing/broadening  
6. ΔH(z) crossover near z=0.45–0.55  
7. Strong tracer independence across BGS, LRG, ELG, QSO voids


# Citations

Jordan Waters
The Gravity of Probability: Replicating Dark Matter Effects Through Quantum Decoherence Curvature
Figshare DOI: 10.6084/m9.figshare.29815934
https://figshare.com/articles/thesis/The_Gravity_of_Probability_i_Replicating_Dark_Matter_Effects_Through_Quantum_Decoherence_Curvature_i_/29815934?file=59563217

Jordan Waters
DESI DR2 VACs Predictions
Fighsare DOI:  10.6084/m9.figshare.30593876
https://figshare.com/articles/preprint/DESI_DR2_VACs_Predictions/30593876?file=59479682

Jordan Waters
Foundations of the Gravity of Probability
Figshare DOI:  10.6084/m9.figshare.30662603
https://figshare.com/articles/preprint/Foundations_of_the_Gravity_of_Probability_A_Decoherence-Driven_Extension_of_General_Relativity/30662603?file=59712056

ORCID
https://orcid.org/0009-0009-0793-8089

Figshare
https://figshare.com/authors/Jordan_Waters/21620558

1. Background

In the Gravity of Probability framework, the total stress–energy tensor is written as:

Tᵤₙᵤᵗᵒᵗᵃˡ = Tᵤₙᵤ + Tᵤₙᵤᵖʳᵒᵇ

where:

Tᵤₙᵤ is the classical stress–energy (baryons, radiation, etc.)

Tᵤₙᵤᵖʳᵒᵇ encodes a small but non-negligible curvature contribution from unrealized quantum amplitudes, modulated by decoherence and entropy

For a homogeneous fluid, we can approximate:

Tᵤₙᵤᵖʳᵒᵇ ≈ κA · Γ(E) · ρ_ψ

where:

κA is the global amplitude that sets the overall strength of the probabilistic curvature

Γ(E) is the decoherence kernel, implemented as a bell-curve function in energy

ρ_ψ is the effective probabilistic or entanglement density, which follows the baryonic (normal-matter) distribution and is scaled by the entanglement fraction f_ent

This repository exposes those ingredients in a simple Python API so that
collaborations (e.g. DESI, Euclid, JWST, lensing groups) can plug GoP into
their existing pipelines.

---

## 2. Installation

### 2.1 Clone the repository

```bash
git clone https://github.com/Jwaters290/GoP-Probabilistic-Curvature.git
cd GoP-Probabilistic-Curvature


---

## Quickstart / Reproduce the main prediction

git clone https://github.com/Jwaters290/GoP-Probabilistic-Curvature.git
cd GoP-Probabilistic-Curvature
pip install -r requirements.txt
jupyter notebook examples/DESI_void_overlay.ipynb

This notebook reproduces the predicted warm-core void profile and z-evolution ramp used for the DESI DR2 VACs predictions.

All simulations in this repo use a single global parameter set
κA = 1.5×10⁻¹⁵, E₀ = 10¹² erg, f_ent = 0.20, A_CP = 0.0245,
fixed as of July 2025 prior to DESI DR2 VACs.
