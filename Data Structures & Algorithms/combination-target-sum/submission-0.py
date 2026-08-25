class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def dfs(i, cur, total):
            if total == target:
                copy = cur[:]
                res.append(copy)

            if i >= len(nums):
                return
            
            for n in range(i, len(nums)):
                if nums[n] + total > target:
                    continue

                cur.append(nums[n])
                dfs(n, cur, nums[n] + total)
                cur.pop()
        

        for j in range(len(nums)):
            if nums[j] > target:
                continue
            dfs(j, [nums[j]], nums[j])


        return res