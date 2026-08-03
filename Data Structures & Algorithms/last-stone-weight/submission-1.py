class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones) != 0 and len(stones) != 1):
            min = 0
            max = 0

            for i in range(len(stones)):
                if stones[i] < stones[min]:
                    min = i
                elif stones[i] > stones[max]:
                    max = i

            if stones[max] == stones[min]:
                stones.remove(stones[max])
                stones.remove(stones[min])
            else:
                stones[max] = stones[max] - stones[min]
                stones.remove(stones[min])
        
        if(stones):
            return stones[0]
        else:
            return 0

            




        