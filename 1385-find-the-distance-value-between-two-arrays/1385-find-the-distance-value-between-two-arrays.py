class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for x in arr1:
            far = True
            for y in arr2:
                if abs(x - y) <= d:
                    far = False
                    break
            if far:
                count += 1
        return count