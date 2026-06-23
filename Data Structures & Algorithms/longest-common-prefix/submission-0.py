class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min = None
        for s in strs:
            if min is None or len(s) < len(min):
                min = s

        hash = {}
        for s in strs:
            index = None
            for i in range(len(min)):
                index = i
                if s[i] == min[i] and hash.get(i) != False:
                    hash[i] = True
                else:
                    hash[i] = False
                    break     

        c = ""
        for k, v in hash.items():
            if v is True:
                c = c + min[k]
            else:
                break;
        return c

