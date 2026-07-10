class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #Solution 1: time complecity o(n^2)
        left = 0
        right = 1

        if len(nums) <= 1:
            return len(nums)

        while left < len(nums) -1 and right < len(nums):
            if nums[right] <= nums[left]:
                right +=1
            else:
                right_val = nums[right]
                left +=1
                nums[right] = nums[left]
                nums[left] = right_val
                right = left + 1
        
        return left + 1


        # Solution 2 (Better, since we don't care about the rest of array, time complexity o(n)): 
        left_p = 0
        right_p = 1
        
        while right_p < len(nums):
            # ONLY do work if when spot a brand new unique number
            if nums[right_p] != nums[left_p]:
                left_p = left_p + 1
                nums[left_p] = nums[right_p]
                
            right_p = right_p + 1

        return left_p + 1