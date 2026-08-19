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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        #brute force
        # q = deque()
        # q.append(root)
        # while q:
        #     size = len(q)
        #     for i in range(size):
        #         t = q.popleft()
        #         if i!=size-1:
        #             t.next = q[0]
        #         else:
        #             t.next = None
        #         if t.left:
        #             q.append(t.left)
        #         if t.right:
        #             q.append(t.right)
        # return root
# common compile time errors
# q.append only accept one param
# there is no null in python


#optimized space complexity
        dummy = Node(0) # to track previous linked node's start
        pre = root # link alread created
        tar = dummy # link need to create
        while pre:
            cur = pre
            tar = dummy
            while cur:
                if cur.left:
                    tar.next = cur.left
                    tar = tar.next
                if cur.right:
                    tar.next = cur.right
                    tar = tar.next
                cur = cur.next
            pre = dummy.next #
            dummy.next = None
        return root
# common compile time errors
#after the logic don't forget to return 