class Solution:
    def checkValidString(self, s: str) -> bool:
        # lets do whatever is needed.
        left = []
        lives = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                left.append(i)
            elif c == ")":
                if left:
                    left.pop()
                elif lives:
                    lives.pop()
                else:
                    return False
                    
            else: # special clause.
                lives.append(i)
        
        while left:
            if not lives:
                return False
            
            if lives[-1] > left[-1]:
                lives.pop()
                left.pop()
            else:
                return False
        return True
        
