# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorder(self,root,l):
        if root:
            self.postorder(root.left,l)
            self.postorder(root.right,l)
            l.append(root.val)
        return l
        
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        a = self.postorder(root,l)
        return a
        