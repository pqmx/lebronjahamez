class Solution:
    def isValid(self, s: str) -> bool:

        parDict = {'(' : ')', '{' : '}', '[' : ']'}

        stack = []
        for c in s:
            if c in parDict:
                stack.append(c)
            if c == ')' or c == '}' or c == ']':
                if parDict[stack[-1]] != c:
                    return False
                stack.pop()

        return True