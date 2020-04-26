class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        x = ''
        for i in s:
            if (i == '(' or i == '[' or i == '{'):
                l.append(i)
            elif (i == ')' or i == ']' or i=='}'):
                if len(l)>0:
                    x = l[len(l)-1]
                else:
                    return False
                if (i == ')' and x == '('):
                    l.pop()
                elif (i == ']' and x == '['):
                    l.pop()
                elif (i == '}' and x == '{'):
                    l.pop()
                else:
                    return False
                    
        if len(l) == 0:
            return True
        else:
            return False
