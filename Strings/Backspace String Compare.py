class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        l = []
        l1 = []
        for i in range(0,len(S)):
            if(S[i] !='#'):
                l.append(S[i])
            if(S[i] == '#'):
                if(((i-1) !=-1) and (len(l)!=0)):
                    l.pop()
        for i in range(0,len(T)):
            if (T[i] != '#'):
                l1.append(T[i])
            if (T[i] == '#'):
                if(((i-1) !=-1) and (len(l1)!=0)):
                    l1.pop()
        if (l == l1):
            return True
        else:
            return False
        