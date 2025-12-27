import random
from collections import Counter


def analytic_probs() -> dict[int, float]:
    counts = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    return {s: c / 36 for s, c in counts.items()}


def monte_carlo_probs(n_rolls: int, seed: int | None = None) -> dict[int, float]:
    rng = random.Random(seed)
    results = []

    for _ in range(n_rolls):
        d1 = rng.randint(1, 6)
        d2 = rng.randint(1, 6)
        results.append(d1 + d2)

    counts = Counter(results)
    return {s: counts.get(s, 0) / n_rolls for s in range(2, 13)}
