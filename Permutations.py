from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # print (list(permutations(nums)))
        l = [list(x) for x in permutations(nums)]
        # print(l)
        return (l)