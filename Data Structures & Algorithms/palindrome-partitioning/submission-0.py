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


        def dfs(i, arr):
            if i >= n:

                
                res.append(arr[:])
                return
            

            #separate
            arr.append(s[i])
            dfs(i + 1, arr)

            arr.pop()

            #include 
            if not arr:
                return

            temp = arr[-1][:]
            temp += s[i]

            if isPalindrome(temp):
                arr[-1] += s[i]
                dfs(i + 1, arr)


        dfs(0, [])

        return res


        