from typing import List

# 977. Squares of a Sorted Array — Easy
# Topics: Two Pointers, Array
# Companies: 

# Original (simple) solution — commented out to preserve the initial approach.
# This uses list comprehension + sort. Kept for reference.
#
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         nums = [i*i for i in nums]
#         nums.sort()
#         return nums
#

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """Return the squares of each number in non-decreasing order using two pointers.

        Two-pointer approach (detailed):
        - Because `nums` is sorted, the largest absolute values are at the ends.
        - Initialize `left` at 0 and `right` at n-1, and an index `idx` at n-1
          to write results from largest to smallest.
        - Compare squares of the values at `left` and `right`. Place the larger
          of the two at `res[idx]`. Move the pointer that produced the larger
          square inward and decrement `idx`.
        - Continue until `left` > `right`.

        This avoids an explicit sort and runs in O(n) time.
        """
        n = len(nums)
        res = [0] * n

        left, right = 0, n - 1
        idx = n - 1

        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]

            if left_sq > right_sq:
                res[idx] = left_sq
                left += 1
            else:
                res[idx] = right_sq
                right -= 1

            idx -= 1

        return res
