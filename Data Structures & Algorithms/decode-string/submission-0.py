class Solution:
    def decodeString(self, s: str) -> str:
        count = []
        letter = []

        cur = ""
        



        for i, c in enumerate(s):
            if c.isdigit():
                if i > 0 and s[i-1].isdigit():
                    prev = count.pop()
                    count.append(prev + c)
                else:
                    count.append(c)
                    
            elif c == "[":
                letter.append(cur)
                cur = ""
            elif c == "]":
                amt = int(count.pop())
                cur = letter.pop() + (cur * amt)
            else:
                cur += c
        return cur
                


                