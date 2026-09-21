class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d, r = deque(), deque()


        # the name fo the game: ban every single person last team remaining wins.
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        


        while d and r:
            if d[0] < r[0]:
                r.popleft()
                i = d.popleft()
                d.append(i + len(senate))
            else:
                d.popleft()
                i = r.popleft()
                r.append(i + len(senate))
        
        return "Dire" if len(d) > len(r) else "Radiant"

        