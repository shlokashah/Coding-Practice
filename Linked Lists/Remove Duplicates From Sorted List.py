# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        l = []
        temp = head
        while(temp):
            l.append(temp.val)
            temp = temp.next
        l = list(dict.fromkeys(l))
        if(len(l) == 0):
            # head.val = ''
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
        return head
            