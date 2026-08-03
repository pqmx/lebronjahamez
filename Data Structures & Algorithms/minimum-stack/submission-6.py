import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)


    def pop(self) -> None:
        val = self.stack.pop()
        self.heap.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # what happens if we pop the min how would we find the next value?
        return self.heap[0]    
        

