class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        sm = sum(nums)
        fin = total - sm
        return fin