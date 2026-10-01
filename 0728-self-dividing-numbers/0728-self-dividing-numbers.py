
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for n in range(left, right + 1):
            ok = True
            for d in str(n):
                d = int(d)
                if d == 0 or n % d != 0:
                    ok = False
                    break
            if ok:
                ans.append(n)
        return ans
