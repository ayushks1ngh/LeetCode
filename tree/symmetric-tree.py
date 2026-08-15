# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.mirror(root.left,root.right)
    def mirror(self,right,left):
        if right is None and left is None:
            return True
        if right is None or left is None:
            return False
        #if values r diff
        if right.val!=left.val:
            return False
        lefts=self.mirror(left.left,right.right)
        rights=self.mirror(right.left,left.right)
        return lefts and rights
        