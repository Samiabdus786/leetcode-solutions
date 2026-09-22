class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        d = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        res = ['']
        for digit in digits:
            res = [a + b for a in res for b in d[digit]]
        return res