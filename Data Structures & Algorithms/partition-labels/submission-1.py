class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # 1. paritition labels choose first char
        # 2. find last instance of that char
        # 3. in between first and last instance if theres another chatacter
        # find the last instance of that char until the last instance of that character is less index than teh instancce of that char baby. 
        

        lastInstance = {}
        
        for i, c in enumerate(s):
            lastInstance[c] = i


        res = []
        i = 0
        while i < len(s):
            c = s[i]
            last = lastInstance[c]
            j = i + 1
            while j <= last:
                if c != s[j] and lastInstance[s[j]] > last:
                    last = lastInstance[s[j]]
                    c = s[j]
                j += 1
            res.append(j - i)
            i = j
                    
        return res

        





        



        

            
        