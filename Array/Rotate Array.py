class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0,len(A)):
            for j in range(i+1,len(A)):
                # print("aya")
                temp = A[i][j]
                A[i][j] = A[j][i]
                A[j][i] = temp
            
        for i in range(len(A)):
            k = 0
            j = len(A)-1
            while(k<j):
                temp = A[i][k]
                A[i][k] = A[i][j]
                A[i][j] = temp
                k = k+1
                j = j-1
        # return A
        
        