# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        s = "".join(str(i) for i in l)
        return(int(s,2))
        