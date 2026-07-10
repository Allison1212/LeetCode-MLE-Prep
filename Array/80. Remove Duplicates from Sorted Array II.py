class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # left_p = 0
        # right_p = 1
        # count = 0

        # if len(nums) <= 2:
        #     return len(nums)
        
        # else:
        #     while right_p < len(nums):
        #         if nums[left_p] == nums[right_p]:
        #             count+=1
        #         else:
        #             if count < 1:
        #                 left_p +=1
        #             else:
        #                 left_p +=2
        #             nums[left_p] = nums[right_p]
        #             count = 0
                    
        #         right_p += 1
        #     return left_p + 1

        if len(nums) <= 2:
            return len(nums)
        
        left_p = 2
        
        for right_p in range(2,len(nums)):
            if nums[right_p] != nums[left_p-2]:
                nums[left_p] = nums[right_p]
                left_p+=1
        
        return left_p