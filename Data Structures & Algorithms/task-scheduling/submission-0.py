class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown_heap = []
        max_heap = []

        num_tasks = Counter(tasks)

        for t, q in num_tasks.items():
            heapq.heappush(max_heap, (-q, t))

        turns = 0
        while max_heap or cooldown_heap:
            if max_heap:
                q, t = heapq.heappop(max_heap)
                q = -q
                for i in range(q):
                    heapq.heappush(cooldown_heap, i * (n + 1))
            
            if cooldown_heap and cooldown_heap[0] <= turns:
                heapq.heappop(cooldown_heap)

            turns += 1

        return turns

            

            

