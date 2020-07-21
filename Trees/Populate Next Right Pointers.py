# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None: 
            return
        queue = []  
        queue.append(root) 
        while(queue):
            s = len(queue)
            for j in range(s):
                node = queue.pop(0)
                if node.left is not None: 
                    queue.append(node.left)
                if node.right is not None: 
                    queue.append(node.right)
            for i in range(len(queue)):
                NP=queue[i+1] if (i+1)<len(queue) else None
                queue[i].next = NP
        return root 