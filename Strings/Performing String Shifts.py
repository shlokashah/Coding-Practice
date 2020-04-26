class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        s1= ""
        for i in range(0,len(shift)):
            l =  shift[i]
            # s = s1 
            s1 = ""
            if (l[0] == 1):
                for i in range(0,len(s)):
                    s1 = s[len(s)-l[1]:]+s[:len(s)-l[1]]
            elif(l[0] == 0):
                for i in range(0,len(s)):
                    s1 = s[l[1]:] + s[:l[1]]
            s = s1
        return s