class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        
        



        # we have an arr with a score to see which one has the most.
        # we get 2 top candidates and update that im thinking of using a maxHeap or some
        start = [0, 0, 0]
        for t in triplets:
            validTriple = all(t[i] <= target[i] for i in range(len(target)))

            if validTriple:
                start = [max(t[i], start[i]) for i in range(len(start))]

            if all(start[i] == target[i] for i in range(len(target))):
                return True
        
        return False
                

