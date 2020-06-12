from collections import Counter
import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        count = Counter(A)
        for i in count:
            if (count[i]>math.floor(len(A)/2)):
                return i
        