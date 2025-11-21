"""
Bell-curve decoherence kernel Gamma(E) used in the GoP framework.

The functional form implemented here is:

    Gamma(E) = A * (E / E0) * exp(-E / E0)

where:
    - E  is a characteristic energy scale (erg),
    - E0 is a global characteristic energy (erg),
    - A  is an overall dimensionless amplitude (default = 1).

The global scaling of the probabilistic curvature term is then handled
via KAPPA_A in gop_constants.py, so that T_prob ~ KAPPA_A * Gamma(E) * rho_Psi.
"""

from __future__ import annotations

import numpy as np

from .gop_constants import E0


def gamma_bell_curve(
    E: float | np.ndarray,
    A: float = 1.0,
    E0_local: float = E0,
) -> float | np.ndarray:
    """
    Compute the bell-curve decoherence kernel Gamma(E).

    Parameters
    ----------
    E : float or numpy.ndarray
        Characteristic energy scale in erg.
    A : float, optional
        Dimensionless amplitude of the bell curve. Default is 1.0.
    E0_local : float, optional
        Characteristic energy scale in erg. Defaults to the global E0.

    Returns
    -------
    Gamma : float or numpy.ndarray
        Dimensionless decoherence kernel Gamma(E).

    Notes
    -----
    - For E << E0, Gamma(E) ~ A * (E/E0).
    - For E ~ E0, Gamma(E) peaks at ~A/e.
    - For E >> E0, Gamma(E) decays exponentially.
    """
    E_arr = np.asarray(E, dtype=float)
    x = E_arr / E0_local
    gamma = A * x * np.exp(-x)
    return gamma
