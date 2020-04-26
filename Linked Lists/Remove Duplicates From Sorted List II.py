# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def duplicate(self,head):
        return (head.next and head.val==head.next.val)
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        d = dummy
        while head:
            if self.duplicate(head):
                while self.duplicate(head):
                    head = head.next
            else:
                d.next = head
                d = d.next
            head = head.next
        d.next = None
        return dummy.next
    