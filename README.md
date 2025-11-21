# GoP-Probabilistic-Curvature
Reference implementation of the Gravity of Probability (GoP) probabilistic curvature term. Includes decoherence kernel Γ(E), global GoP constants, and Tᵐᵤₙᵤ^{prob} calculator for use in cosmology, lensing, and galaxy modeling.


# GoP-Probabilistic-Curvature

Reference implementation of the **Gravity of Probability (GoP)** probabilistic
curvature term \(T_{\mu\nu}^{\rm prob}\).

This repository provides a minimal, usable Python implementation of the
**decoherence kernel** \(\Gamma(E)\), global GoP parameters, and a simple
stress–energy calculator that maps \((E, \rho_b, z)\) to an effective
probabilistic stress–energy tensor for use in cosmology, lensing, and galaxy
dynamics.

---

## 1. Background

In the Gravity of Probability framework, the total stress–energy tensor is
written as

\[
T_{\mu\nu}^{\rm total} = T_{\mu\nu} + T_{\mu\nu}^{\rm prob},
\]

where

- \(T_{\mu\nu}\) is the classical stress–energy (baryons, radiation, etc.),
- \(T_{\mu\nu}^{\rm prob}\) encodes a small but non-negligible curvature
  contribution from unrealized quantum amplitudes, modulated by decoherence
  and entropy.

At the level of a homogeneous fluid, we can schematically write

\[
T_{\mu\nu}^{\rm prob} \;\sim\; \kappa A \, \Gamma(E)\, \rho_\Psi,
\]

where

- \(\kappa A\) is a global amplitude,
- \(\Gamma(E)\) is a decoherence kernel (here implemented as a bell-curve
  function in energy),
- \(\rho_\Psi\) is an effective probabilistic / entanglement density that
  tracks baryonic structure with an entanglement fraction \(f_{\rm ent}\).

This repository exposes those ingredients in a simple Python API so that
collaborations (e.g. DESI, Euclid, JWST, lensing groups) can plug GoP into
their existing pipelines.

---

## 2. Installation

### 2.1 Clone the repository

```bash
git clone https://github.com/Jwaters290/GoP-Probabilistic-Curvature.git
cd GoP-Probabilistic-Curvature
