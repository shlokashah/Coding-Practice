class Solution:
    def romanToInt(self, A: str) -> int:
        num = 0
        for i in range(0,len(A)):
            if(A[i] == 'I'):
                if(i == (len(A)-1)):
                    num = num + 1
                else:
                    if((A[i+1])=='V' or (A[i+1])=='X' or (A[i+1])=='L' or (A[i+1])=='C' or (A[i+1])=='D' or (A[i+1])=='M'):
                        num = num - 1
                    else:
                        num = num + 1
            elif(A[i] == 'V'):
                if(i == (len(A)-1)):
                    num = num + 5
                else:
                    if((A[i+1])=='X' or (A[i+1])=='L' or (A[i+1])=='C' or (A[i+1])=='D' or (A[i+1])=='M'):
                        num = num - 5
                    else:
                        num = num + 5
            elif(A[i] == 'X'):
                if(i == (len(A)-1)):
                    num = num + 10
                else:
                    if((A[i+1])=="L" or (A[i+1])=='C' or (A[i+1])=='D' or (A[i+1])=='M'):
                        num = num - 10
                    else:
                        num = num + 10
            elif(A[i] == 'L'):
                if(i == (len(A)-1)):
                    num = num + 50
                else:
                    if((A[i+1])=='C' or (A[i+1])=='D' or (A[i+1])=='M'):
                        num = num - 50
                    else:
                        num = num + 50
            elif(A[i] == 'C'):
                if(i == (len(A)-1)):
                    num = num + 100
                else:
                    if((A[i+1])=='D'  or (A[i+1])=='M'):
                        num = num - 100
                    else:
                        num = num + 100
            elif(A[i] == 'D'):
                if(i == (len(A)-1)):
                    num = num + 500
                else:
                    if((A[i+1])=='M'):
                        num = num - 500
                    else:
                        num = num + 500
            else:
                num = num + 1000
        return num