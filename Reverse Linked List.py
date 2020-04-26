# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = ListNode()
        prev = None
        temp = head
        while(temp):
            flag = ListNode()
            flag = temp.next
            temp.next = prev
            prev = temp
            temp = flag
        return prev
        