class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hsh = {}
        for h in hand:
            hsh[h] = hsh.get(h, 0) + 1
        
        hand.sort()

        for h in hand:
            if h in hsh and h - 1 not in hsh: # we found our base.
                for i in range(1, groupSize):
                    testNum = h + i
                    if testNum not in hsh:
                        return False
                    else:
                        hsh[testNum] -= 1
                        if hsh[testNum] <= 0:
                            del hsh[testNum]
        
        return True

                    

        
            
           

