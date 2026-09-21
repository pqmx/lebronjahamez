class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            if not stack:
                stack.append(a)
                continue
            
            isOpposite =(a < 0 and stack[-1] > 0) or (a > 0 and stack[-1] < 0)
            if isOpposite:
                if abs(a) == abs(stack[-1]):
                    stack.pop()
                    continue
                elif abs(a) < abs(stack[-1]):
                    continue
                else:
                    stack.pop()
                    stack.append(a)   
            else:
                stack.append(a)
        
        return stack