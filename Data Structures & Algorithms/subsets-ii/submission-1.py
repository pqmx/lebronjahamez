class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        visited = set()
        nums.sort()
        for n in nums:
            for i in range(len(res)):
                copy = res[i][:]
                copy.append(n)
                copyTuple = tuple(copy)
                if copyTuple in visited:
                    continue

                visited.add(copyTuple)
                res.append(copy)
        
        return res
