class Solution:
    
   
    
    def isHappy(self, n: int) -> bool:
        sum_1 = n
        sum_2 = n
        
        def squasum(num: int):
            s = 0
            while(num):
                s = s +( num%10) * (num%10)
                # print(num%10)
                num = int(num/10)
                # print(s)
            return s
    
        while True:
            sum_1 = squasum(sum_1)
            sum_2 = squasum(squasum(sum_2))
            if (sum_1 != sum_2):
                continue
            else:
                break
        return (sum_2 == 1)
        
            
        
        