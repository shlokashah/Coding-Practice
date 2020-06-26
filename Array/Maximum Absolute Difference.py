class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        m1 = []
        m2 = []
        for i in range(len(A)):
            m1.append(A[i]+i)
            m2.append(A[i]-i)
        return(max(max(m1)-min(m1),max(m2)-min(m2)))
