class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []


        def isPalindrome(s):
            check = len(s) // 2 
            last = len(s) - 1
            for i in range(check):
                if s[i] != s[last - i]:
                    return False
            return True


        # get i j 
        # if palindrome -> extend j or move on from i



        def dfs(i, j, arr):

            if i >= n or j >= n:
                if i == j:
                    # that means if its the same index last operation was successful. and both moved on.
                    res.append(arr)
                return
            while i > j:
                j+= 1


            temp = arr[:]

            dfs(i, j + 1, temp) #extend
            if isPalindrome(s[i : j + 1]):
                arr.append(s[i : j + 1]) 
                dfs(j + 1, j + 1, arr) #move on.


                

                




        dfs(0, 0, [])
        return res




        