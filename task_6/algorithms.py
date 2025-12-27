def greedy_algorithm(items: dict, budget: int):
    candidates = []
    for name, data in items.items():
        calories_per_cost = data["calories"] / data["cost"]

        candidates.append(
            {
                "name": name,
                **data,
                "efficiency": calories_per_cost,
            }
        )

    candidates.sort(key=lambda x: x["efficiency"], reverse=True)

    total_calories = 0
    total_cost = 0
    chosen_items = []

    for item in candidates:
        if total_cost + item["cost"] <= budget:
            chosen_items.append(item["name"])
            total_cost += item["cost"]
            total_calories += item["calories"]

    return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(names)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_cost = costs[i - 1]
            item_cal = calories[i - 1]

            if item_cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item_cost] + item_cal)
            else:
                dp[i][w] = dp[i - 1][w]

    max_calories = dp[n][budget]

    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name = names[i - 1]
            chosen_items.append(item_name)
            w -= costs[i - 1]

    total_cost = sum(items[item]["cost"] for item in chosen_items)

    return chosen_items, max_calories, total_cost
