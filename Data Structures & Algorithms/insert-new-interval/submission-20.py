class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval
        hasInserted = False
        for curStart, curEnd in intervals:
            arr = [curStart, curEnd]
            if not res:
                res.append(arr)
                continue


            prevStart, prevEnd = res[-1]

            # merge newInterval -> 
            if not hasInserted and prevEnd >= newStart:
                newArr = [min(prevStart, newStart), max(prevEnd, newEnd)]
                res.pop()
                res.append(newArr)
                hasInserted = True

            # only append if we can
            if not hasInserted and prevEnd <= newStart <= curStart:
                    hasInserted = True
                    res.append(newInterval)

            # lastly append the cur element but we must still check.
            prevStart, prevEnd = res[-1]
            if prevEnd >= curStart:
                arr = [min(prevStart, curStart), max(prevEnd, curEnd)]
                res.pop()
                res.append(arr)
            else:
                res.append(arr)
            


        if not hasInserted:
            # we can merge or append.
            if not res:
                res.append(newInterval)
            prevStart, prevEnd = res[-1]
            if prevEnd >= newStart:
                newArr = [min(prevStart, newStart), max(prevEnd, newEnd)]
                res.pop()
                res.append(newArr)
            else:
                res.append(newInterval)

        return res

            
            
        




    
        