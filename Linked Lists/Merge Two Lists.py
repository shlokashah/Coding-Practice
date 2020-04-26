# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = []
        head_1 = l1
        temp = head_1
        head_2 = l2
        while(temp):
            l.append(temp.val)
            temp = temp.next  
        temp = head_2
        while(temp):
            l.append(temp.val)
            temp = temp.next
        l = sorted(l)
        head = ListNode()
        if(len(l)==0):
            head.val=''
            return head
        head.val = l[0]
        head.next = None
        flag = head
        for i in range(1,len(l)):
            temp = ListNode()
            temp.val = l[i]
            temp.next = None
            flag.next = temp
            flag = temp
        return head