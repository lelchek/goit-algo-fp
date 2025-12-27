from math import sqrt
import matplotlib.pyplot as plt


def print_comparison_table(mc: dict[int, float], analytic: dict[int, float]) -> None:
    print(f"{'Sum':>5} | {'MC %':>8} | {'Analytic %':>11} | {'Abs err %':>10}")
    print("-" * 46)

    sq_error = 0.0

    for s in range(2, 13):
        mc_p = mc[s]
        an_p = analytic[s]
        err = abs(mc_p - an_p)
        sq_error += (mc_p - an_p) ** 2

        print(f"{s:>5} | {mc_p*100:>7.3f} | {an_p*100:>10.3f} | {err*100:>9.3f}")

    rmse = sqrt(sq_error / 11)
    print("-" * 46)
    print(f"RMSE: {rmse:.6f} ({rmse*100:.4f}%)")


def plot_probs(mc: dict[int, float], analytic: dict[int, float], n_rolls: int) -> None:
    sums: list | None = list(range(2, 13))
    mc_vals = [mc[s] for s in sums]
    an_vals = [analytic[s] for s in sums]

    x = range(len(sums))
    width = 0.4

    plt.figure()
    plt.bar([i - width / 2 for i in x], mc_vals, width, label="Monte Carlo")
    plt.bar([i + width / 2 for i in x], an_vals, width, label="Analytic")

    plt.xticks(list(x), sums)
    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.title(f"Sum of Two Dice (N={n_rolls})")
    plt.legend()
    plt.tight_layout()
    plt.show()
