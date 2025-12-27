from tree_model import Node
from traversals import dfs_tree, bfs_tree
from tree_draw import animate_traversal


def main():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    dfs_order_ids = dfs_tree(root)
    animate_traversal(root, dfs_order_ids)

    bfs_order_ids = bfs_tree(root)
    animate_traversal(root, bfs_order_ids, cmap_name="Greens_r")


if __name__ == "__main__":
    main()
