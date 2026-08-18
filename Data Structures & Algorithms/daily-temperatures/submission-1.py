
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = [] # pair: [index, temp]


        for i, t in enumerate(temperatures):
            if not stack:
                stack.append([i, t])
                continue
            while stack and t > stack[-1][1]: # has stack greater than stack.
                sIndex, _ = stack.pop()
                res[sIndex] = i - sIndex
        return res
            


                



        