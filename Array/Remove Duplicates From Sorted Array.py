class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dif_num=1
        if nums==[]:
            return 0

        for i in range(len(nums)):
            if(i+1<len(nums)):
                if nums[i]<nums[i+1]:
                    nums[dif_num]=nums[i+1]
                    dif_num+=1
            
        # print(nums)
        return dif_num
        