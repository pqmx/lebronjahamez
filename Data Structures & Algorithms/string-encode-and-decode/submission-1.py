class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + str(s)
        return string


    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):
            # check number length.
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            
            start = i + 1
            end = start + int(length) - 1
            words.append(s[start : end + 1])
            i = end + 1
        return words


                #5alone
