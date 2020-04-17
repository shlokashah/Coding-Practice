class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        

    def push(self, x: int) -> None:
        self.l.append(x)
        

    def pop(self) -> None:
        self.l.pop()
        

    def top(self) -> int:
        a = self.l[-1]
        return a
        
        

    def getMin(self) -> int:
        b = min(self.l)
        return b
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()