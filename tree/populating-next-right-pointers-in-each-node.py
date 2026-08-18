"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        node = root
        while node.left:
            nextLineNode = node.left
            while node.next:
                node.left.next = node.right
                node.right.next = node.next.left
                node = node.next
            node.left.next = node.right
            node = nextLineNode
        return root