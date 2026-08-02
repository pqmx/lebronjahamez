class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []


        # lets fill prefix.
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
                continue
            
            prefix.append(nums[i] * prefix[-1])


        # -1, 0, 0, 0, 0
        #  3, 6, 6, 0, 0
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                postfix.append(nums[i])
                continue
            
            postfix.append(nums[i] * postfix[-1])

        postfix = postfix[::-1]

        print(prefix)
        print(postfix)

        for i in range(len(nums)):
            preval = 1
            postval = 1
            if i > 0:
                preval = prefix[i - 1]
            if i < len(nums) - 1:
                postval = postfix[i + 1]
                
            nums[i] = preval * postval
        
        return nums
            

