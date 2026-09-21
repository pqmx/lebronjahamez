class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d, r = deque(), deque()


        # the name fo the game: ban every single person last team remaining wins.
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.appendleft(i)
            else:
                d.appendleft(i)
        
        print(d)
        print(r)
        while d and r:
            if d[0] < r[0]:
                r.popleft()
            else:
                d.popleft()
        



        return "Dire" if len(d) > len(r) else "Radiant"

        