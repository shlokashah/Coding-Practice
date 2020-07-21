# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        N = 0
        l = []
        while(A):
            l.append(A.val)
            N = N+1
            A = A.next
        # print(l)
        a = N//B
        answer = []
        for i in range(0,N,B):
            answer.append(l[i:i+B])
        # print(answer)
        l = []
        for i in range(0,len(answer),2):
            answer[i] = answer[i][::-1]
        for i in answer:
            l.extend(i)
        # print(l)
        head = ListNode(l[0])
        head.next = None
        temp = head
        for i in range(1,len(l)):
            flag = ListNode(l[i])
            flag.next = None
            temp.next = flag
            temp = flag
        return head
        
