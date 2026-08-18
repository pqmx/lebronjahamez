class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars = cars.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in cars:
            curTime = (target-p) / s
            stack.append(curTime)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
                



                


        


        