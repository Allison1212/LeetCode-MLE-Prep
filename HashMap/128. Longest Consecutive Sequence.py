class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        for n in nums_set:
            if n-1 not in nums_set:
                count = 1
                while n+1 in nums_set:
                    count+=1
                    n+=1
                max_length = max(count,max_length)
        return max_length

        # 用set 去重
        # 只需要找开始
        # sort 就会有nlogn
        # 因为有if 拦截，所以是O(N)
