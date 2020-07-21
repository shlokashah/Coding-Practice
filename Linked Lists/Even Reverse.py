# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        odd = []
        even = []
        odd.append(A.val)
        A = A.next
        i = 1
        while(A):
            i = i+1
            if(i%2==0):
                even.append(A.val)
            else:
                odd.append(A.val)
            A = A.next
        even = even[::-1]
        print(odd,even)
        l = max(len(odd),len(even))
        
        head = ListNode(odd[0])
        head.next = None
        temp = head