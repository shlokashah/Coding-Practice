class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 0):
                    col.append(j)
        for i in range(0,len(matrix)):
            if(0 in matrix[i]):
                matrix[i] = [0]*len(matrix[i])
        for i in range(len(matrix)):
            for j in col:
                matrix[i][j] = 0
        print(col)
        print(matrix)
        