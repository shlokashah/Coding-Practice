# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        temp = head
        count = 0
        print(temp)
        while(temp):
            count = count + 1
            temp = temp.next
        print(count)
        if(count %2 ==0):
            middle = math.ceil((count+1)/2)
        else:
            middle = math.ceil((count+1)/2)
        i = 1
        l = []
        temp = head
        while(i <middle):
            temp = temp.next
            i = i+1
        # while(temp):
            # l.append(temp.val)
            # temp = temp.next
        return(temp)
            
            
        