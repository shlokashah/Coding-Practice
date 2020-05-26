class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = [0 for i in range(0,len(nums))]
        answer[0] = nums[0]
        for i in range(1,len(nums)):
            answer[i] = max(answer[i-1]+nums[i],nums[i])
        return max(answer)
        