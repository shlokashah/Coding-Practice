# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
        return l
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = []
        a = self.inorder(root,l)
        return a
    
        