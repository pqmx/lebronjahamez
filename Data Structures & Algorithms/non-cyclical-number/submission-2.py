class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        visited = set()
        while n != 1 and n not in visited:
            total = 0
            while n >= 10:
                remainder = n % 10
                total += (remainder * remainder)
                n //= 10
            total += n * n
            n = total
            visited.add(n)
            print(visited)
        

        if n == 1:
            return True
        return False


        
        