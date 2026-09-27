class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sort(start, end):
            if end - start > 2:
                midpoint = (start + end) // 2
                sort(start, midpoint)
                sort(midpoint + 1, end)
            elif end - start == 2:
                first = nums[start]
                sercond = nums[start + 1]
        