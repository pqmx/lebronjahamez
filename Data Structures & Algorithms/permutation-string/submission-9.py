class Solution:
    def checkInclusion(self, sub: str, reg: str) -> bool:
        if len(sub) > len(reg):
            return False

        l = 0
        r = len(sub) - 1
        subH = {}
        regH = {}

        for c in sub:
            if c not in subH:
                subH[c] = 1
            else:
                subH[c] += 1

        for i in range(len(sub)):
            if reg[i] not in regH:
                regH[reg[i]] = 1
            else:
                regH[reg[i]] += 1

        while r < len(reg):
            allEqual = True

            if len(regH) == len(subH):
                for c in regH:
                    if c in subH and regH[c] == subH[c]:
                        continue
                    allEqual = False
                    break
            else:
                allEqual = False

            if allEqual:
                return True

            leftChar = reg[l]
            if regH[leftChar] == 1:
                del regH[leftChar]
            else:
                regH[leftChar] -= 1

            l += 1
            r += 1

            if r >= len(reg):
                return False

            rightChar = reg[r]
            if rightChar not in regH:
                regH[rightChar] = 1
            else:
                regH[rightChar] += 1

        return False