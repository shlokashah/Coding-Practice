# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: 
            return
        queue = []  
        queue.append(root) 
        i = 0
        answer = [[] for j in range(10000)]
        answer[i].append(root.val)
        i = i +1
        current = []
        while(queue):
            s = len(queue)
            for j in range(s):
                node = queue.pop(0)
                if node.left is not None: 
                    queue.append(node.left)
                    current.append(node.left.val)
                if node.right is not None: 
                    queue.append(node.right)
                    current.append(node.right.val)
            answer[i] = current
            current = []
            i = i + 1
        answer = filter(None, answer)
        return answer