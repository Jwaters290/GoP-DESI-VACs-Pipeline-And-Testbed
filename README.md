# Gravity of Probability (GoP)
**Keywords:** gravity-of-probability, decoherence, probabilistic-curvature, alternative-gravity, S8-tension, DESI DR2

# GoP-Probabilistic-Curvature

Reference implementation of the Gravity of Probability (GoP) probabilistic curvature term Tᵤₙᵤᵖʳᵒᵇ. Includes decoherence kernel Γ(E), global GoP constants, and Tᵐᵤₙᵤ^{prob} calculator for use in cosmology, lensing, and galaxy modeling.

# Gravity of Probability (GoP) — Probabilistic Curvature Kernel


This repository contains the official Python implementation of the GoP probabilistic curvature tensor Tᵘₙᵤᵖʳᵒᵇ, 
including the decoherence kernel Γ(E), global GoP constants, and tools for computing rotation curves, 
gravitational lensing, void thermodynamics, and large-scale structure predictions. This is the primary 
codebase used for GoP predictions in DESI, Euclid, CMB, and lensing analyses.

# Citations

Jordan Waters
The Gravity of Probability: Replicating Dark Matter Effects Through Quantum Decoherence Curvature
Figshare DOI: 10.6084/m9.figshare.29815934

Jordan Waters
DESI DR2 VACs Predictions
Fighsare DOI:  10.6084/m9.figshare.30593876

Jordan Waters
Foundations of the Gravity of Probability
Figshare DOI:  10.6084/m9.figshare.30662603

ORCID
https://orcid.org/0009-0009-0793-8089

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
