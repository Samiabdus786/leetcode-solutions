class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        a = 0
        o = 0
        for x in d.values():
            a += x // 2 * 2
            if x % 2:
                o = 1
        return a + o