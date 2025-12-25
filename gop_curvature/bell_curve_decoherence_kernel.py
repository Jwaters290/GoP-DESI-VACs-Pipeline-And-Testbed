"""
Bell-curve decoherence kernel Γ(E) used in the GoP framework.

Canonical form (GoP "core-four"):

    Γ(E) = κA * E * exp(1 - E/E0)

where:
  - E is a characteristic energy scale (erg or an energy proxy used consistently),
  - E0 is the global characteristic energy scale (erg),
  - κA is the global amplitude (effective units depend on Γ(E) convention).

This form peaks at E = E0, with Γ(E0) = κA * E0.
"""

from __future__ import annotations

import numpy as np

from .gop_constants import KAPPA_A, E0


def gamma_bell_curve(
    E: float | np.ndarray,
    kappaA: float = KAPPA_A,
    E0_local: float = E0,
) -> float | np.ndarray:
    """
    Compute the canonical GoP bell-curve decoherence kernel Γ(E).

    Parameters
    ----------
    E : float or numpy.ndarray
        Characteristic energy scale (erg or consistent proxy).
    kappaA : float, optional
        Global amplitude κA. Defaults to KAPPA_A from gop_constants.py.
    E0_local : float, optional
        Characteristic energy scale E0. Defaults to global E0.

    Returns
    -------
    Gamma : float or numpy.ndarray
        Decoherence kernel Γ(E).

    Notes
    -----
    - Peaks at E = E0_local.
    - Γ(E0_local) = kappaA * E0_local.
    - Shape is bell-like in log space; decays exponentially for E >> E0.
    """
    E_arr = np.asarray(E, dtype=float)
    x = E_arr / E0_local
    return kappaA * E_arr * np.exp(1.0 - x)
