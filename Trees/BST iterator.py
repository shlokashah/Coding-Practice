# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # l = []
    def __init__(self, root: TreeNode):
        head = root
        self.l = []
        self.l = self.inorder(root,self.l)
        print(self.l)
        
    def inorder(self,root,l):
        if root is None:
            return
        self.inorder(root.left,l)
        l.append(root.val)
        self.inorder(root.right,l)
        return l

    def next(self) -> int:
        """
        @return the next smallest number
        """
        n = self.l.pop(0)
        return n
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.l:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()