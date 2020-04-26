# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        temp = head
        count = 0
        while(temp):
            count = count+1
            temp = temp.next
        k = count - n +1
        i = 1
        if(count == 1 and k==1):
            head.val=''
            return head
        flag = head
        temp = flag
        if(i == k):
            head = temp.next
            return head
        while(i<k):
            temp = flag
            flag = flag.next
            i = i +1
        temp.next = flag.next
        return head
            