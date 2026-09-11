class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #init heap
        maxHeap= []
        visited = set()
        res = []
        i = 0
        while i < len(nums):
            while len(maxHeap) < k:
                visited.add(nums[i])
                heapq.heappush(maxHeap, (nums[i] * -1))
                i += 1
            
            res.append(maxHeap[0] * -1)
            
            if maxHeap[0] == (nums[i - k] * -1):
                heapq.heappop(maxHeap)
                visited.remove(nums[i - k])
            elif i < len(nums) and nums[i] in visited:
                i += 1
                continue
            else:
                removedIndex = maxHeap.index(nums[i - k] * -1)
                maxHeap.pop(removedIndex)
                visited.discard(nums[i - k])
        
        return res

