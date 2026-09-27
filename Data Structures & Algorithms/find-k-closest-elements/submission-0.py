class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []

        for a in arr:
            aX = abs(a - x)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (-aX, a))
            else:
                if aX < -maxHeap[0][0] or (aX == -maxHeap[0][0] and a < maxHeap[0][1]):
                    heapq.heappop(maxHeap)
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, (-aX, a))

        res = [n for _, n in maxHeap]
        res.sort()
        return res