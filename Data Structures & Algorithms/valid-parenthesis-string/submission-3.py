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
                    if lives and lives[-1] > left[-1]:
                        lives.pop()
                    else:
                        left.pop()
                else:
                    if lives:
                        lives.pop()
                    else:
                        return False
            else: # special clause.
                lives.append(i)
        

        return len(left) == 0
        
