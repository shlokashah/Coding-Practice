# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, root):
        queue = [] 
        queue.append(root)
        s = []
        m = 0
        while(queue):
            l = len(queue)
            for i in range(0,l):
                node = queue.pop(0)
                if node.left:
                    s.append(node.val)
                if node.right:
                    s.append(node.val)
            m = max(m,sum(s))
            s = []
        return m
