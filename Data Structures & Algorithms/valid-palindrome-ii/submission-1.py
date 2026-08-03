class Solution:
    def validPalindrome(self, s: str) -> bool:
        deletedOne = False
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if deletedOne:
                    return False
                else:
                    deletedOne = True
                    if s[left] != s[right - 1]:
                        left += 1
                    else:
                        left -= 1
            left += 1
            right -=1 
        
        return True
        