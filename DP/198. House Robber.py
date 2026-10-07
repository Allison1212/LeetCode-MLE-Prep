class Solution:
    def rob(self, nums: list[int]) -> int:
        # rdp[i] = max(dp[i-2] + nums[i], dp[i-1])
        # 每个点只记住到目前为止的optimal
        # 然后主要记住前i-2 和i-1 时 的optimal 在那基础做判定

        rob1 = rob2 = 0
        for n in nums:
            temp = max(rob1 + n,rob2)
            rob1 = rob2
            rob2 = temp
        return rob2