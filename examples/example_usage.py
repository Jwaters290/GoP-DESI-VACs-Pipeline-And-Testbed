"""
Minimal usage example for the GoP probabilistic curvature implementation.
"""

from gop_curvature import (
    gamma_bell_curve,
    compute_tmunu_prob,
    KAPPA_A,
    E0,
)


def main() -> None:
    # Example parameters (toy values)
    E = E0               # erg, at the characteristic scale
    rho_b = 1.0e-27      # g/cm^3, a cosmological baryon density scale
    z = 0.5              # redshift

    Gamma = gamma_bell_curve(E)
    T_prob = compute_tmunu_prob(E, rho_b, z=z)

    print("Using KAPPA_A =", KAPPA_A)
    print("E =", E, "erg")
    print("rho_b =", rho_b, "g/cm^3")
    print("z =", z)
    print()
    print("Gamma(E) =", Gamma)
    print("T_prob (4x4) =")
    print(T_prob)
    print()
    print("Energy density contribution T00 =", T_prob[0, 0], "erg/cm^3")


if __name__ == "__main__":
    main()
