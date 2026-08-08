class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            arr.append(0)
            for i in range(len(nums) - 4, -1, -1):
                arr[i] += max(arr[i + 2], arr[i + 3])
            
            return max(arr[0], arr[1])

        return max(helper(nums[1:]), helper(nums[:-1]))

            

            


            

        


    
        




