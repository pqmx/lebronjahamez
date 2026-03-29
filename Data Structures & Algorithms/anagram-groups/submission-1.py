class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dictS = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            if key not in dictS:
                dictS[key] = []
            dictS[key].append(s)
            
            
        output = []
        for key, val in dictS.items():
            output.append(val)
        return output

        