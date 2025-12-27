from probabilities import analytic_probs, monte_carlo_probs
from visualization import print_comparison_table, plot_probs


def main():
    N_small = 100
    N_big = 1_000_000
    seed = 42

    analytic = analytic_probs()
    mc_small = monte_carlo_probs(N_small, seed)
    mc_big = monte_carlo_probs(N_big, seed)

    print(f"\n=== Monte Carlo with N={N_small} ===")
    print_comparison_table(mc_small, analytic)
    plot_probs(mc_small, analytic, N_small)

    print(f"\n=== Monte Carlo with N={N_big} ===")
    print_comparison_table(mc_big, analytic)
    plot_probs(mc_big, analytic, N_big)


if __name__ == "__main__":
    main()
