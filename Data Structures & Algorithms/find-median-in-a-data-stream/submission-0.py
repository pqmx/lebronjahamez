class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)

        

    def findMedian(self) -> float:
        res = None
        middle = len(self.arr) // 2 - 1
        if len(self.arr) % 2 == 0:
            res = (self.arr[middle] + self.arr[middle + 1]) / 2
        else: # odd
            res = float(self.arr[len(self.arr) // 2])
        
        return res


        