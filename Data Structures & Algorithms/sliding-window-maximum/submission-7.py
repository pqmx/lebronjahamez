class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #init heap
        maxHeap= []

        res = []
        i = 0
        while i < len(nums):
            while len(maxHeap) < k:
                heapq.heappush(maxHeap, (nums[i] * -1))
                i += 1
            
            res.append(maxHeap[0] * -1)
            
            if maxHeap[0] == (nums[i - k] * -1):
                heapq.heappop(maxHeap)
            elif i < len(nums) and nums[i] == nums[i - k]:
                continue
            else:
                removedIndex = maxHeap.index(nums[i - k] * -1)
                maxHeap.pop(removedIndex)
        
        return res

