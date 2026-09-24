class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = set()
        for i in range(n):
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
                        res.add((firstNum, secondNum, nums[l], nums[r]))
                        l += 1
                        r-= 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r- 1] == nums[r]:
                            r -= 1
        return [list(r) for r in res]



                

                


                

        



        

        