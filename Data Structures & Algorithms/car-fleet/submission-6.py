class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for p, s in cars:
            curTime = (target-p) / s
            if stack and curTime >= stack[-1]:
                stack.append(curTime)
                
        
        return len(stack)
                



                


        


        