class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sum_cost = nums[0]
        res = nums[1:]
        res.sort()
        return sum_cost + sum(res[:2])

    # Time Complexity: O(n log n) – sorting the `res` list dominates
    # the runtime for n = len(nums).
    # Space Complexity: O(n) – the slice `res = nums[1:]` creates an
    # additional list proportional to the input size.