# GoP-Probabilistic-Curvature
Reference implementation of the Gravity of Probability (GoP) probabilistic curvature term. Includes decoherence kernel Γ(E), global GoP constants, and Tᵐᵤₙᵤ^{prob} calculator for use in cosmology, lensing, and galaxy modeling.


# GoP-Probabilistic-Curvature

Reference implementation of the Gravity of Probability (GoP) probabilistic curvature term Tᵤₙᵤᵖʳᵒᵇ.

This repository provides a minimal, usable Python implementation of the decoherence kernel Γ(E), the global GoP parameters, and a simple stress–energy calculator that maps (E, ρ_b, z) to an effective probabilistic stress-energy tensor for use in cosmology, lensing, and galaxy dynamics.

The description above was originally written in LaTeX. This version uses plain Unicode characters for clarity.

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
