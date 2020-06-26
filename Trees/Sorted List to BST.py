# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def create_tree(self,tree):
        if len(tree)==0:
            return 
        mid = int(len(tree)/2)
        root = TreeNode()
        root.val = tree[mid]
        root.left = self.create_tree(tree[:mid])
        root.right = self.create_tree(tree[mid+1:])
        return root
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        print(l)
        tree = self.create_tree(l)
        return tree