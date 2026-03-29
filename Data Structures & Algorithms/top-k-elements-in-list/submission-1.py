class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # [1: 1, 2: 2, 3: 3]
        for n in set(nums):
            freq[count[n]].append(n)
        
     # [[], [1], [2], [3]]
        output = []
        for i in range(len(freq) - 1, -1, -1):
                for n in freq[i]:
                    k -= 1
                    output.append(n)

                if k == 0:
                    return output

            


        