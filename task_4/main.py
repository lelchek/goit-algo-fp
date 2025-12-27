from typing import Optional
import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


Pos = dict[str, tuple[float, float]]


class Node:
    def __init__(self, key, color="skyblue"):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


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


def draw_tree(tree_root: Node) -> None:
    tree = nx.DiGraph()
    pos: Pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw_networkx(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()


def make_tree_from_heap(heap_list: list[int]) -> Node | None:
    if not heap_list:
        return None

    nodes = [Node(item) for item in heap_list]

    for i, current_node in enumerate(nodes):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            current_node.left = nodes[left_index]

        if right_index < len(nodes):
            current_node.right = nodes[right_index]

    return nodes[0]


def main():
    heap_list = [10, 1, 5, 20, 4, 15, 11, 2, 7, 9, 4, 3]
    heapq.heapify(heap_list)

    root = make_tree_from_heap(heap_list)
    if root is not None:
        draw_tree(root)


if __name__ == "__main__":
    main()
