class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        parDict = {'(' : ')', '{' : '}', '[' : ']'}

        stack = []
        for c in s:
            if c in parDict:
                stack.append(c)
            if c == ')' or c == '}' or c == ']':
                if not stack or parDict[stack[-1]] != c:
                    return False
                stack.pop()

        return not stack