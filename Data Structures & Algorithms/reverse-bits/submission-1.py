class Solution:
    def reverseBits(self, n: int) -> int:
        return n.split("")[::-1].join("")
        