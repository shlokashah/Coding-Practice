class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if(nums.count(0)>1):
            return True
        if(sum(nums)-sum(set(nums)) == 0):
            return False
        else:
            return True
        
        