class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand via center
        res = ""
        
        for i in range(len(s)):
            # ODD CASES
            r = i
            l = i

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            
            # check our results.
            l += 1
            r -= 1
            word = s[l : r + 1]
            length = len(word)

            if length > len(res):
                res = word
                

            
            # EVEN CASES
            l = i
            r = i + 1

            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break;

            l += 1
            r -= 1
            word = s[l : r + 1]
            length = len(word)
            
            if length > len(res):
                res = word

       
        return res
        


        