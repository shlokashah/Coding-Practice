class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(0,len(nums)):
            if nums[i] in d:
                d[nums[i]] = d[nums[i]]+1
            else:
                d[nums[i]] = 1
        print(d)
        for i,v in d.items():
            if (v == 1):
                return (i)
                # return d.key
        