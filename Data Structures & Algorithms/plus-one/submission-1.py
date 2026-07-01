class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        start = True
        for i in range(len(digits) - 1, -1, -1):
            if start: # first num
                start = False
                if digits[i] == 9:
                    carry = 1
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
            elif digits[i] + carry == 10:
                carry = 1
                digits[i] = 0
            else:
                digits[i] += carry
                return digits

        if digits[i] == 0:
            digits.insert(0, 1)
        
        return digits


        