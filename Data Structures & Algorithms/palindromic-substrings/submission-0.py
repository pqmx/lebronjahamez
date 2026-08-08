class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            l = i
            r = i
            
            # this is for odd cases.
            while l >= 0 and r < len(s):
                #check for 2 char characters
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break;

            #even cases.
            l = i
            r = i + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
                else:
                    break;

        return res

    # a aa a aaa aa a
        