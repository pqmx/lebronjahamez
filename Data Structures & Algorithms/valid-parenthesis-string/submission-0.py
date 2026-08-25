class Solution:
    def checkValidString(self, s: str) -> bool:
        # lets do whatever is needed.
        stack = []
        lives = 0

        for c in s:
            if c == '(':
                stack.append('(')

            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    if lives:
                        lives -= 1
                    else:
                        return False
                

            
            else: # special clause.
                lives += 1
        

        return len(stack) <= lives
        
