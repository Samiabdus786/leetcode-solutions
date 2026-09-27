class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # Convert negative number to 32-bit unsigned value
        if num < 0:
            num += 2 ** 32

        chars = "0123456789abcdef"
        ans = ""

        while num > 0:
            remainder = num % 16
            ans = chars[remainder] + ans
            num //= 16

        return ans