class Solution:
    def convertToTitle(self, A: int) -> str:
        l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        answer = ""
        n = A
        while(n!=0):
            answer = answer + l[(n-1)%26]
            n = (n-1)//26
        return (answer[::-1])