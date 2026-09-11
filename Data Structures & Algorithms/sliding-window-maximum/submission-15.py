class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #init heap
        maxHeap= []
        res = []

        for i, n in enumerate(nums):
            # i = 0, 1 2
            heapq.heappush(maxHeap, (-n, i))

            if i + 1 >= k: # 
                while maxHeap[0][1] <= i - k:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0][0])
        
        return res

