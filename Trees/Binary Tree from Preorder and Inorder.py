# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if(len(inorder)==0 or len(preorder)==0):
            return 
        root = TreeNode()
        index = inorder.index(preorder[0])
        root.val = preorder.pop(0)
        root.left = self.buildTree(preorder,inorder[:index])
        root.right = self.buildTree(preorder,inorder[index+1:])
        return root