from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        answer,dummy = c.most_common(1)[0]
        return answer
        