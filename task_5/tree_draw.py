from tree_model import Node
import networkx as nx
import matplotlib.pyplot as plt
from colors import generate_colors

Pos = dict[str, tuple[float, float]]


def add_edges(
    graph: nx.DiGraph,
    node: Node | None,
    pos: Pos,
    x: float = 0,
    y: float = 0,
    layer: int = 1,
):
    if node is None:
        return graph

    graph.add_node(node.id, color=node.color, label=node.val)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        l = x - 1 / 2**layer
        pos[node.left.id] = (l, y - 1)
        add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        r = x + 1 / 2**layer
        pos[node.right.id] = (r, y - 1)
        add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root: Node) -> tuple[nx.DiGraph, Pos]:
    tree = nx.DiGraph()
    pos: Pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    return tree, pos


def animate_traversal(root, order_ids, cmap_name="Blues_r"):
    tree, pos = draw_tree(root)

    current_colors = {n: "#CCCCCC" for n in tree.nodes()}
    # labels = nx.get_node_attributes(tree, "label")
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    final_colors = generate_colors(order_ids, cmap_name)

    plt.figure(figsize=(8, 5))

    for step, node_id in enumerate(order_ids):
        plt.clf()
        plt.title(f"Step {step + 1}")

        current_colors[node_id] = final_colors[node_id]

        color_list = [current_colors[n] for n in tree.nodes()]

        nx.draw_networkx(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=1000,
            node_color=color_list,
        )

        plt.pause(0.5)

    plt.show()
