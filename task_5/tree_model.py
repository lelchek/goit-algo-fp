from typing import Optional
import uuid


class Node:
    def __init__(self, key, color="skyblue"):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())
