class Solution:
    def reverseString(self, s: List[str]) -> None:
        if s == "":
            return
        left = 0
        right = len(s) - 1
        while abs(left - right) > 1:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left +=1 
            right -= 1

        