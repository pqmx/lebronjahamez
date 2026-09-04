class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []

        for i in range(len(intervals)):
            curStart, curEnd = intervals[i]

            if not res: # res is empty.
                res.append(intervals[i])
                continue # we dont go into res yet.

            if res:
                prevStart, prevEnd = res[-1] # top of arr.
                if curStart > prevEnd:
                    res.append(intervals[i])
                    continue

                newArr = [min(curStart, prevStart), max(prevEnd, curEnd)]
                res.pop()
                res.append(newArr)

        return res
           

                
                






           
