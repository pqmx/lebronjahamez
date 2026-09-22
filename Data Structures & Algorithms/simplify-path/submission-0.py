class Solution:
    def simplifyPath(self, path: str) -> str:
        path = [x for x in path.split("/") if x]
        path.reverse()

        res = []


        while path:
            cur= path.pop()
            c = cur[0]
            if c == ".":
                length = len(cur)
                if length == 1:
                    continue
                elif length == 2:
                    if res:
                        res.pop()
                else:
                    res.append(cur)
            else:
                res.append(cur)
            
        
        return "/" + "/".join(res)

            


        

        

        
        
