# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l = []
        while(head):
            l.append(head.val)
            head = head.next
        l.sort()
        if(len(l)==0):
            return head
        head = ListNode()
        head.val = l[0]
        head.next = None
        flag = head
        for i in range(1,len(l)):
            temp = ListNode()
            temp.val = l[i]
            flag.next = temp
            flag = temp
            temp.next = None
        return head
        