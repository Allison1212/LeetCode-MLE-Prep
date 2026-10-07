class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        res = acc_sum = nums[0]
        for i in range(1,len(nums)):
            acc_sum += nums[i]
            if nums[i] >= acc_sum:
                acc_sum = nums[i]
            res = max(res,acc_sum)
        return res
    # brute force 肯定写的出来
    # 下一步就是看怎么哪些start point 是不值得search的
    # 如果当前值　＞ 前面的sum就可以扔掉前面的accumulate sum了