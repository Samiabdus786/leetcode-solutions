class Solution:
    def findMissingAndRepeatedValues(self, g):
        n = len(g)
        c = [0] * (n * n + 1)

        for r in g:
            for x in r:
                c[x] += 1

        for i in range(1, n * n + 1):
            if c[i] == 2:
                a = i
            elif c[i] == 0:
                b = i

        return [a, b]