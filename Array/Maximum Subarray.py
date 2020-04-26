class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_index = 0
        max_done = 0
        if len(nums)==1:
            return nums[0]
        if (all (x<0 for x in nums)):
            return max(nums)
        for i in range(0,len(nums)):
            max_index = max_index + nums[i]
            if max_index < 0:
                max_index = 0
            if max_done < max_index :
                max_done = max_index
        return max_done
            
        
        