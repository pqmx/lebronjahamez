class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        # lets sort.
        nums = sorted(nums)

        n = len(nums)

        for i in range(n):
            target = -nums[i] #first pointer
            #second pointer.
            j = i + 1
            #third pointer
            k = j + 1
            while j < n and k < n: # they have not reached the bounds.
                new_target = target - nums[j]
                if nums[k] != new_target:
                    k += 1
                else: #we got it!
                    combinations.append([nums[i], nums[j], nums[k]])
                if k >= n: # k is already at the end. we did not find a match. push j next.
                    j += 1
                    k = j + 1


        return combinations


        
            
            