# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        points = set()
        while head:
            if head not in points:
                points.add(head)
            else:
                return head
            head = head.next
        return None
        

        