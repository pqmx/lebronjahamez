class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = 0
        e = len(s) - 1
        while st != e:
            if not s[e].isalpha():
                e -= 1
                continue
            if not s[st].isalpha():
                st += 1
                continue
            
            if s[st].lower() != s[e].lower():
                return False
            e -= 1
            st += 1
        return True
