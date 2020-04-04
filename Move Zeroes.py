class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(0,len(nums)):
            if (nums[i] != 0):
                nums[count] = nums[i]
                count = count + 1
        while(count<len(nums)):
            nums[count] = 0
            count = count+1
        return (nums)