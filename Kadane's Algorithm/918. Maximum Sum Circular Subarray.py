class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        # max_sum = nums[0]
        
        # # brute force
        # for i in range(len(nums)):
        #     count = 0
        #     cum_sum = 0
        #     j = i
        #     while count < len(nums):
        #         j = j % len(nums)
        #         cum_sum +=nums[j]
        #         max_sum = max(max_sum,cum_sum)
        #         j += 1
        #         count +=1

        # return max_sum

        # max and min solution 
        max_sum = float('-inf')
        curr_sum_max = 0
        min_sum = float('inf')
        curr_sum_min = 0
        total = 0

        for i in range(len(nums)):
            curr_sum_max+= nums[i]
            curr_sum_min+= nums[i]

            curr_sum_max = max(curr_sum_max,nums[i])
            curr_sum_min = min(curr_sum_min,nums[i])

            max_sum = max(curr_sum_max,max_sum)
            min_sum = min(curr_sum_min,min_sum)
            total += nums[i]
        if total == min_sum:
            return max_sum
        else:
            return max(max_sum,total-min_sum)
        
        # Time complexity O(N)
        # Space complexity 0(1)
        # Gap:
            # 其实当我看到test case 已经想到了，max subarray 可以出现两种情况一个是正常的max 在中间，还有就是max 在两边
            # 在两边可以转化成， minimize middle， total - min 就是max了

        