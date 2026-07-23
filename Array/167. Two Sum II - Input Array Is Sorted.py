class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            sum_up = numbers[left] + numbers[right]
            if sum_up == target:
                return [left+1,right+1]
            elif sum_up > target:
                right -= 1
            else:
                left += 1
    
    # When see Pairing, Boundary Evaluation, or Interval Constraints $\rightarrow$ Reach for Inward-Closing Pointers (Collision Pointers).
    # When see Filtering, In-Place Overwriting, or Continuous Subarray/Substring Lengths $\rightarrow$ Reach for Fast & Slow Pointers (Same-Direction Pointers).