# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        l = []
        while A:
            l.append(A.val)
            A = A.next
        l = sorted(l)
        # print(l)
        head = ListNode(0)
        head.val = l[0]
        head.next = None
        flag = head
        for i in range(1,len(l)):
            temp = ListNode(0)
            temp.val = l[i]
            flag.next = temp
            temp.next = None
            flag = temp
        return head