class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = [[0 for j in range(A)] for i in range(A)]
        rstart =  0
        rend = A
        cstart = 0
        cend = A
        count = 1
        while((rstart < rend) and (cstart < cend)):
            for i in range(cstart,cend):
                matrix[rstart][i] = count 
                count = count + 1
            rstart = rstart + 1
            for i in range(rstart,rend):
                matrix[i][cend-1] = count
                count = count + 1
            cend = cend - 1
            if(rstart<rend):
                for i in range(cend-1,cstart-1,-1):
                    matrix[rend-1][i] = count
                    count = count + 1
                rend = rend - 1
            if(cstart<cend):
                for i in range(rend-1,rstart-1,-1):
                    matrix[i][cstart] = count
                    count = count + 1
                cstart = cstart + 1
            
        return matrix
            
