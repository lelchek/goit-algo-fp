from collections import deque
from tree_model import Node


def dfs_tree(tree_root: Node):
    order = []
    stack = [tree_root]

    while stack:
        current = stack.pop()
        order.append(current.id)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return order


def bfs_tree(tree_root: Node):
    order = []
    queue = deque([tree_root])

    while queue:
        current = queue.pop()
        order.append(current.id)

        if current.left:
            queue.appendleft(current.left)

        if current.right:
            queue.appendleft(current.right)

    return order
