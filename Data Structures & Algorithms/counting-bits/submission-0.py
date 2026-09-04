class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            bit = int(bin(i)[2:])
            result = 0
            while bit >= 10:
                result += bit % 10
                bit = bit // 10
            result += bit



            res.append(result)

        return res