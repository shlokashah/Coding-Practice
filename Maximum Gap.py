class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        diff = []
        if(len(nums)==0):
            return 0
        if(len(nums)==1):
            return 0
        for i in range(1,len(nums)):
            diff.append(nums[i]-nums[i-1])
        return(max(diff))
            
            
        