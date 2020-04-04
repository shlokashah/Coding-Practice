class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = [str(i) for i in digits]
        num = int(''.join(digit))
        num = num +1
        num = str(num)
        answer = [int(i) for i in num]
        return answer
            
        