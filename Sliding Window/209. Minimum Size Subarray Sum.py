class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # My first version
        # min_size = len(nums)

        # left = 0
        # right = 0

        # current_sum = 0

        # if sum(nums) < target:
        #     return  0
        # while current_sum < target:
        #     current_sum = current_sum + nums[right]
        #     right +=1
        # min_size = right - left 

        # while right < len(nums):
        #     current_sum = current_sum + nums[right] - nums[left]
        #     left +=1
        #     while current_sum - nums[left] >= target:
        #         current_sum = current_sum - nums[left]
        #         left +=1
        #     print(right,left)
        #     min_size = min(min_size,right - left + 1)
        #     right +=1

        # while current_sum - nums[left] >= target:
        #     current_sum = current_sum - nums[left]
        #     left +=1
        #     min_size = min(min_size,right - left)
            

        # return min_size

        # Second version 
        min_size = len(nums)

        left = 0

        current_sum = 0

        if sum(nums) < target:
            return 0

        for i in range(len(nums)):
            current_sum += nums[i]
            while current_sum >= target:
                min_size = min(min_size,i-left+1)
                current_sum -= nums[left]
                left+=1
        
        return min_size

        #实现代码的时候不要想着打补丁
        # 先找出主题步伐： for i in range(len(nums)):
        # 再考虑要变动的节点情况
        
        Optimal:
        use float('inf') for initial size
        class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # 设一个不可能达到的大数作为占位符
        min_size = float('inf')
        left = 0
        current_sum = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            
            # 只要满足条件，就无情地挤水分（做减法）
            while current_sum >= target:
                min_size = min(min_size, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        # 如果还是初始的无穷大，说明从没凑够过 target，返回 0
        return 0 if min_size == float('inf') else min_size