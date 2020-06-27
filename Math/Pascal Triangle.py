class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # i = 0
        answer =[]
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if(j==0 or j==i):
                    temp.append(1)
                else:
                    temp.append(answer[i-1][j]+answer[i-1][j-1])
            answer.append(temp)
        return answer
                    
        