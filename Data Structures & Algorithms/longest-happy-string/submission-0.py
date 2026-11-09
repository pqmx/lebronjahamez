class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        

        s = ""
        total = [[a, "a"], [b, "b"], [c, "c"]]
        h = []


        for n, ch in total:
            heapq.heappush(h, (-n, ch))
        
        while h:
            n, ch = heapq.heappop(h)
            if n == 0:
                break
            if len(s) >= 2 and s[-1] == s[-2] == ch:
                if not h:
                    break
                n2, ch2 = heapq.heappop(h)
                if n2 == 0:
                    break
                s += ch2
                if n2 + 1 < 0: # hasn't reached 0 -> -n2 - 1
                    heapq.heappush(h, (n2 + 1, ch2))
                heapq.heappush(h, (n, ch))
            else:
                s += ch
                if n + 1 < 0:
                    heapq.heappush(h, (n + 1, ch))
        return s
                    
                    


            
            

                

