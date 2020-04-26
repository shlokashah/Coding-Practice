class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for i in range(0,len(arr)):
            if ((arr[i]+1) in arr):
                count = count +1
        return count 