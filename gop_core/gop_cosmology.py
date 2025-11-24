import numpy as np

def compute_pk_gop(k_array, k0=0.1, sigma_k=0.03, amplitude=0.03):
    """
    GoP P(k) modifier for early-phase DESI Lyα/LSS VAC testing.
    This replaces the toy model in scripts/gop_lss_earlytest.py.

    Parameters
    ----------
    k_array : numpy array
        Array of k values [h/Mpc].
    k0 : float
        Center of GoP-induced bump. Default = 0.1 h/Mpc.
    sigma_k : float
        Width of bump. Default = 0.03 h/Mpc.
    amplitude : float
        Height of bump. Default = 0.03 (i.e., 3%).

    Returns
    -------
    numpy array
        Multiplicative factor f(k) such that:
        P_GoP(k) = f(k) * P_LCDM(k)
    """
    return 1.0 + amplitude * np.exp(-0.5 * ((k_array - k0) / sigma_k)**2)
