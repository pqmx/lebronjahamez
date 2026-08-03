class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) != 0 and len(stones) != 1):
            s1 = stones[0]
            s2 = stones[1]
            if s1 == s2:
                stones.remove(s1)
                stones.remove(s2)
                continue
            if s1 < s2:
                stones[1] = s2 - s1
                stones.remove(s1)
            else:
                stones[0] = s1 - s2
                stones.remove(s2)
        
        if len(stones) == 0:
            return 0
        else:
            return stones[0]




        