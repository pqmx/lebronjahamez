class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        letterDict = {
 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6,
 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
 'y': 25, 'z': 26
}
        dictS = {}
        for s in strs:
            value= 0
            for c in s:
                value += letterDict[c]
            if value not in dictS:
                dictS.update({value: [s]})
            else:
                dictS[value].append(s)
            
        output = []
        for key, val in dictS.items():
            output.append(val)
        return output

        