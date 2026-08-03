class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cs=ms=nums[0]
        for i in nums[1:]:
            cs=max(i,cs+i)
            ms=max(ms,cs)
        return ms
