class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        string = ""
        max = 0
        for n in s:
            if n not in letters:
                letters.add(n)
                string += n
            else:
                if len(string) > max:
                    max = len(string)
                letters = set(n)
                string = n
        return max