# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A_nodes, B_nodes = [], set()
        while headA:
            A_nodes.append(headA)
            headA = headA.next
        while headB:
            B_nodes.add(headB)
            headB = headB.next
        for node in A_nodes:
            print(node)
            if node in B_nodes:
                return node
        return None
            
            
        