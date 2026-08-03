class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        stack = []
        tokens.reverse()
        while tokens:
            val = tokens.pop()
            if self.convertable(val):
                stack.append(int(val))
            else:
                # sign
                second = stack.pop()
                first = stack.pop()
                if val == '+':
                    stack.append(first + second)
                elif val == '-':
                    stack.append(first - second)
                elif val == '*':
                    stack.append(first * second)
                elif val == '/':
                    stack.append(first / second)
        
        return stack[0]
    def convertable(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False