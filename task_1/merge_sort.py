from typing import Optional
from linked_list import Node


def get_middle(head: Node) -> Node:
    slow: Optional[Node] = head
    fast: Optional[Node] = head.next

    while fast is not None and fast.next is not None:
        if slow is None:
            break
        slow = slow.next
        fast = fast.next.next

    if slow is None:
        return head

    return slow


def merge_sorted(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    dummy = Node(0)
    tail = dummy

    while a is not None and b is not None:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a is not None else b
    return dummy.next


def merge_sort(head: Optional[Node]) -> Optional[Node]:
    if head is None or head.next is None:
        return head

    mid = get_middle(head)
    right = mid.next
    mid.next = None

    left_sorted = merge_sort(head)
    right_sorted = merge_sort(right)

    return merge_sorted(left_sorted, right_sorted)
