class Solution:
    def titleToNumber(self, s: str) -> int:
        d = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        sum = 0
        for i in s:
            sum = (26*sum)+(d.index(i)+1)
        return sum
            
        