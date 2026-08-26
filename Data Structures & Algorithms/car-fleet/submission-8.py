class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda x: x[0])

        stack = []

        
        stack = []

        for i in range(len(cars) - 1, -1, -1):
            p, s = cars[i]
            time = (target - p) / s
            stack.append(time)
            if len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()
            
        return len(stack)
        
        




        