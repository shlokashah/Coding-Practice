class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        n.sort()
        l = len(n)
        if(len(n)%2==0):
            s = n[int((l/2)-1)] + n[int(l/2)]
            return (s/2)
        elif(len(n)%2!=0):
            # s = n[((l+1)/2)-1]
            s = n[(int(((l+1)/2)-1))]
            return s
        