class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def sort_arr(nums):
            if len(nums) <= 1:
                return
            mid = len(nums) // 2

            left_arr = nums[:mid]
            right_arr = nums[mid:]

            sort_arr(left_arr)
            sort_arr(right_arr)


            i = j = k = 0
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    nums[k] = left_arr[i]
                    i += 1
                else:
                    nums[k] = right_arr[j]
                    j += 1
                k += 1


            while i < len(left_arr):
                nums[k] = left_arr[i]
                k += 1
                i += 1
            
            while j < len(right_arr):
                nums[k] = right_arr[j]
                k += 1
                j += 1
        
        sort_arr(nums)
        return nums
