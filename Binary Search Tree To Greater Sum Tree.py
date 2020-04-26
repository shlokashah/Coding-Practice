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
    
    def change_value(self,root,d):
        if(root):
            self.change_value(root.left,d)
            temp = d[root.val]
            root.val = temp
            self.change_value(root.right,d)
        return root
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        l = []
        i = self.inorder(root,l)
        tree = i
        i = i[::-1]
        count = 0
        greater_sum = []
        s = 0
        for j in range(0,len(i)):
            s = s + i[j]
            greater_sum.append(s)
        greater_sum = greater_sum[::-1]
        d = {tree[i]: greater_sum[i] for i in range(len(tree))}
        print(d)
        node = self.change_value(root,d)
        return(node)
        
        