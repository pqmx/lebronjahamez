class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub, reg = None, None
        if len(s1) < len(s2):
            sub = s1
            reg = s2
        else:
            sub = s2
            reg = s1

        # setting window constraints which will always be lenght of the substring.
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
            # lets compare both of our hashes.
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
            rightChar = reg[r]

            if regH[leftChar] == 1:
                del regH[leftChar]
            else:
                regH[leftChar] -= 1

            if regH[rightChar] == 1:
                del regH[rightChar]
            else:
                regH[rightChar] -= 1

            l += 1
            r += 1

            if r >= len(reg):
                return False

            leftChar = reg[l]
            rightChar = reg[r]

            if leftChar not in regH:
                regH[leftChar] = 1
            else:
                regH[leftChar] += 1


            if rightChar not in regH:
                regH[rightChar] = 1
            else:
                regH[rightChar] += 1


            print(l, r)
            

        return False
        