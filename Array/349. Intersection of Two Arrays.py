class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect = set(nums1) - (set(nums1) - set(nums2))
        return list(intersect)