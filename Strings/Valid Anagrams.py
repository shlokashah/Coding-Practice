class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        r = sorted(t)
        if(len(s)!=len(r)):
            return False
        for i in range(len(s)):
            if(s[i]!=r[i]):
                return False
        return True
        
        