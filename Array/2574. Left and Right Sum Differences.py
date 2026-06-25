class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        result_lst = [0] * len(nums)
        i = 0
        while i < len(nums):

            left = sum(nums[:i])
            right = sum(nums[i+1:])
            print(left,right)
            result_lst[i] = abs(left - right)
            i = i + 1
        return  result_lst
    

    #Syntax: list[start:stop]
    # Start: Included in the result.
    # Stop: Excluded from the result.