class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            firstNum = nums[i]
            for j in range(i + 1, n):
                secondNum = nums[j]
                remain = target - (firstNum + secondNum)
                
                
                # two pointers
                l, r = j + 1, n - 1

                # l cannot overlap r since it is 2 distinct nums (must)
                while l < r:
                    amt = nums[l] + nums[r]
                    if amt > remain:
                        r -= 1
                    elif amt < remain:
                        l += 1
                    else:
                        res.append([firstNum, secondNum, nums[l], nums[r]])
                        break
        return res



                

                


                

        



        

        