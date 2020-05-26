class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3: 
            answer = [0, 1, 2]
            return answer [n]
        
        answer = [0, 1, 2] + [0]* (n -2)  
        for i in range(3, n+1):
            answer[i] = answer[i-1] + answer[i-2] 
        
        return answer[n]
            
        