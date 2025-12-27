from graph import Graph
from dijkstra_algo import dijkstra


def main():
    g = Graph()

    graph_map = {
        "A": {"B": 5, "C": 10},
        "B": {"D": 3, "E": 9},
        "C": {"D": 2},
        "D": {"E": 4, "F": 8},
        "E": {"F": 2},
    }

    for u, neighbors in graph_map.items():
        for v, weight in neighbors.items():
            g.add_edge(u, v, weight)

    start_node = "A"
    print(f"Start: {start_node}\n")

    shortest_paths = dijkstra(g, start_node)

    print(f"{'Node':<10} | {'Distance':<10}")
    print("-" * 25)

    for vertex, distance in shortest_paths.items():
        print(f"{vertex:<10} | {distance:<10}")


if __name__ == "__main__":
    main()
