"""
Global constants and parameters for the Gravity of Probability (GoP)
probabilistic curvature implementation.

All values are in cgs units unless otherwise noted.
"""

# Fundamental physical constants (cgs)
C_LIGHT: float = 2.99792458e10   # cm/s
G_NEWTON: float = 6.67430e-8     # cm^3 g^-1 s^-2

# Global GoP parameters (dimensionless or in cgs where appropriate)
#
# These are the parameter values used consistently across the GoP
# galaxy, lensing, and cosmology applications.
#
# kappa_A is the overall amplitude scaling of the probabilistic curvature term.
KAPPA_A: float = 1.5e-15   # dimensionless effective amplitude

# Characteristic energy scale in the bell-curve decoherence kernel Gamma(E).
E0: float = 1.0e12         # erg

# Entanglement fraction: fraction of baryonic density that effectively
# participates in the probabilistic scalar field rho_Psi.
F_ENT: float = 0.20        # dimensionless

# CP asymmetry parameter carried over from LHCb-scale modeling.
# Sign and exact magnitude can be refined in future versions.
A_CP: float = 0.0245       # dimensionless (~2.45%)
