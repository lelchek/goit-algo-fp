from algorithms import greedy_algorithm, dynamic_programming


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    budget = 105

    g_items, g_cal, g_cost = greedy_algorithm(items, budget)
    print(f'Greedy: {g_cal} kcal, {g_cost}$; {", ".join(g_items)}')

    dp_items, dp_cal, dp_cost = dynamic_programming(items, budget)
    print(f'DP: {dp_cal} kcal, {dp_cost}$; {", ".join(dp_items)}')


if __name__ == "__main__":
    main()
