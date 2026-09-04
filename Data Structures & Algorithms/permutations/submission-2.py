class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(cur, dup):

            # if cur already has same length its a permutation.
            if len(cur) >= len(nums):
                print(cur)
                res.append(cur)
                return
            

            for n in nums:
                if n in dup:
                    continue
                else:

                    #add it back.
                    cur.append(n)
                    dup.add(n)
                    c = cur[:]
                    d = set(c)

                    dfs(c, d)

                    #remove it now.
                    dup.remove(n)
                    cur.pop()


        dfs([], set())
        print(res)
        return res