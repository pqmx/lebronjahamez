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
            k = n - 1
            while j < k:
                amt = nums[i] + nums[j] + nums[k]
                if amt > 0:
                    k -= 1
                elif amt < 0:
                    j += 1
                else:
                    combinations.append([nums[i], nums[j], nums[k]])
                    j +=1
                    k -= 1


        return combinations


        
            
            