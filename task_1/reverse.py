from typing import Optional
from linked_list import Node


def reverse_list(head: Optional[Node]) -> Optional[Node]:
    prev: Optional[Node] = None
    current: Optional[Node] = head

    while current is not None:
        next_node: Optional[Node] = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev
