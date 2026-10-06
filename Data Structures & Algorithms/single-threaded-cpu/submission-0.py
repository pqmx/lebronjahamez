class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []
        

        for i, (e, p) in enumerate(tasks):
            heapq.heappush(pending, (e, p, i))


        time = 0
        res = []

        while available or pending:
            if not pending:
                time = max(time, available[0][0])
            else:
                time = max(time, pending[0][0])

            while pending and pending[0][0] <= time:
                e, p, i = heapq.heappop(pending)
                heapq.heappush(available, (e + p, i))


            # problem -> how ccan we keep track of things usch as 0:1000 and 2
            if available: # our times are now valid in the enqueue.
                _, i = heapq.heappop(available)
                res.append(i)
        
        return res


