class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        if len(l)!=0:
            return(len(l[-1]))
        else:
            return 0
        