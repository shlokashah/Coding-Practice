# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,l):
        if root:
            self.inorder(root.left,l)
            l.append(root.val)
            self.inorder(root.right,l)
        return l
    
    def isValidBST(self, root: TreeNode) -> bool:
        l = []
        a = self.inorder(root,l)
        if(len(a)==1):
            return True
        if(len(list(set(a)))==1 or len(list(set(a)))<len(list(a)) ):
            return False
        if (sorted(a) == a):
            return True
        else:
            return False
        
        
        
        