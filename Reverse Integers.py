import math
class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        y = 0
        if(len(str(x))==1):
            return(x)
        if(x in range((-int(math.pow(2,31))),int(math.pow(2,31))-1)):
            if(x<0):
                count = 1
                y = abs(x)
                s = str(y)
                s = s[::-1]
                if(int(s) in range((-int(math.pow(2,31))),int(math.pow(2,31))-1)):
                    return("-"+s.lstrip('0'))
                else:
                    return (0)
            else:
                y = x
                s = str(y)
                s = s[::-1]
                if(int(s) in range((-int(math.pow(2,31))),int(math.pow(2,31))-1)):
                    return(s.lstrip('0'))
                else:
                    return (0)
        else:
            return(0)
