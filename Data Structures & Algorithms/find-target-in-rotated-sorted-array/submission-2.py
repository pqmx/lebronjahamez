class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r + l)// 2
            if nums[mid] == target:
                return mid

            # lets check which side does the middle value belong to.
            if nums[l] <= nums[mid]:
                if nums[l] > target:
                    l = mid + 1 # pivot to right
                else:
                    r = mid - 1 # set to the left side.



            else: # rightside.
                # nums[l] > nums[mid]
                if nums[r] > target:
                    l = mid + 1
                else: # nums[r] <= target
                    r = mid - 1

        return -1





