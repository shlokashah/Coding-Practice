class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                temp = nums[j]
                nums[i] = nums[j]
                i = i+1
                print(nums)
        return i
                    
                
        