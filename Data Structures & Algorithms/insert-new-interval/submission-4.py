class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newStart, newEnd = newInterval
        hasInserted = False
        for start, end in intervals:
            arr = [start, end]
            

            if not hasInserted:
                if res and res[-1][1] < newInterval[0] and newInterval[1] < arr[0]:
                    hasInserted = False
                    res.append(newInterval)


            if newStart < end and not hasInserted:
                arr = [start, max(end, newEnd)]
                hasInserted = True
            
            if not res:
                res.append(arr)
                continue
            


            curStart, curEnd = arr
            prevStart, prevEnd = res[-1]

            if curStart < prevEnd:
                newArr = [min(curStart, prevStart), max(prevEnd, curEnd)]
                res.pop()
                res.append(newArr)
            else:
                res.append(arr)

    
        return res

            
            
        




    
        