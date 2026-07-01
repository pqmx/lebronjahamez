class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits = digits[:: -1]
        i = 0
        while carry:
            if i == len(digits):
                digits.append(1)
                break
            elif digits[i] >= 9:
                digits[i] = 0
            else:
                digits[i] += carry
                carry = 0
                break
            i += 1


        return digits[::-1]

        
        