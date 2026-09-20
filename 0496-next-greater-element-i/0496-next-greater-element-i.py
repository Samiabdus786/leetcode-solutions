class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        d = {}

        for x in nums2:
            while st and st[-1] < x:
                d[st.pop()] = x
            st.append(x)

        return [d.get(x, -1) for x in nums1]