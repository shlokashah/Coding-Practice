# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,root1):
        if(root is None and root1 is None):
            return True
        # if(root is None or root1 is None):
        #     return False
        if(root and root1):
            if(root.val == root1.val):
                return(self.check(root.left,root1.right) and self.check(root.right,root1.left))
        return False  
    def isSymmetric(self, root: TreeNode) -> bool:
        a = self.check(root,root)
        return a