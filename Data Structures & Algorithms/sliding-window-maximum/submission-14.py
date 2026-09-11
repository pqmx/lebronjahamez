class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #init heap
        maxHeap= []
        visited = set()
        res = []
        for i in range(len(nums)):
            while len(maxHeap) < k:
                heapq.heappush(maxHeap, (-nums[i]))
            
            res.append(-maxHeap[0])
            
            if maxHeap[0] == (-nums[i - k]):
                heapq.heappop(maxHeap)
            else:
                removedIndex = maxHeap.index(-nums[i - k])
                maxHeap.pop(removedIndex)
        
        return res

