class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        
        cur = 0
        projected = 0
        while l <= r and r < len(height):
            if height[r] >= height[1]:
                l = r
                cur += projected
                projected = 0
            else:
                projected += height[l] - height[r]
            
            
            r += 1
        return cur


        
            


