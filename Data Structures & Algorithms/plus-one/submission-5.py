class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        digits = digits[:: -1]
        i = 0
        while carry:
            if digits[i] > 9:
                digits[i] = 0
            else:
                digits[i] + carry
                carry = 0
                return digits
            i += 1

        if digits[0] == 0:
            digits.append(1, 0)
        