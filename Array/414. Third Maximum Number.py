class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sort_nums = list(nums_set)
        sort_nums.sort()
        if len(sort_nums) >= 3:
            return sort_nums[-3]
        else:
            return sort_nums[-1]