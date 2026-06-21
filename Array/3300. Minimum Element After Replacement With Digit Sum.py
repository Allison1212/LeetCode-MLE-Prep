class Solution:
    def minElement(self, nums: List[int]) -> int:

        for n in range(0, len(nums)):
            n_list = [int(i) for i in list(str(nums[n]))]
            nums[n] = sum(n_list)
        return min(nums)
