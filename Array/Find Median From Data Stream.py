class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()
    def findMedian(self) -> float:
        length = len(self.l)
        if(length%2!=0):
            middle = int((length+1)/2)
            return(self.l[middle-1])
        else:
            middle_1 = int(length/2)
            middle_2 = int((length/2)-1)
            return((self.l[middle_1]+self.l[middle_2])/2)
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()