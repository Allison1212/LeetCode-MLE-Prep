# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:

#         left = 0
#         right = left + k

#         max_v = sum(nums[left:right])

#         while right <= len(nums):
#             avg_v = sum(nums[left:right])
#             if avg_v >= max_v:
#                 max_v = avg_v
            
#             left = left + 1
#             right = right + 1

#         return max_v/k

# Slice window solution (avoid sum all the elements)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_value = max_value = sum(nums[0:k])

        for i in range(0,len(nums)-k):
            print(i)
            print(f'before{k_value}')
            k_value = k_value - nums[i]
            k_value = k_value + nums[i+k]
            print(f'after{k_value}')
            if k_value >= max_value:
                max_value = k_value
        
        return max_value/k