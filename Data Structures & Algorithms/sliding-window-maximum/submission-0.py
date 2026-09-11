class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #init heap
        maxHeap= []
        res = []
        i = 0
        while i < len(nums):
            # i = 0
            while len(maxHeap) < k:
                heapq.heappush(maxHeap, nums[i] * -1)
                i += 1
            # i = 3
            
            res.append(maxHeap[0] * -1)
            removedEl = maxHeap.index(nums[i - 3] * -1)
            maxHeap.pop(removedEl)
        
        return res

