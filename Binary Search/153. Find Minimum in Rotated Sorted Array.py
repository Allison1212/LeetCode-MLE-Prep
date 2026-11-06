class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = float('inf')
        
        l,r = 0,len(nums)-1
       

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1
            res = min(nums[m],res)
        return res

        # Time complexity O(logn)
        # Space complexity O(1)
    
    # 这题其实已经通过分类讨论想到单调性，也把两个主要条件都写出来了， 但是忽略了left == right index 的情况
    # 其实就是simplify 逻辑，只找 sorted 部分，然后search 另一边