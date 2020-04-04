class Solution:
    def addBinary(self, a: str, b: str) -> str:
        integer_sum = int(a,2) + int(b,2)
        return(bin(integer_sum).replace("0b",""))
        