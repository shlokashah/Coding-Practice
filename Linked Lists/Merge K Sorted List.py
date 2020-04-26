# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = []
        for i in lists:
            temp = i
            while(temp):
                l.append(temp.val)
                flag = temp
                temp = temp.next
        # print(sorted(l))
        l = sorted(l)
        head = ListNode()
        if(len(l) == 0):
            head.val = ''
            return head
        head = ListNode()
        head.val = l[0]
        head.next = None
        flag = head
        for i in range(1,len(l)):
            temp = ListNode()
            temp.val = l[i]
            temp.next = None
            flag.next = temp
            flag = temp
        return(head)
            
        
            
                    