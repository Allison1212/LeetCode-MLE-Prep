class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # My solution
        if len(nums) == 1:
            return True
        else:
            r = len(nums) -1
            l = r -1
            while l >= 0:
                if l + nums[l] >= r:
                    r = l
                l -= 1
            
            return r == l+1
        
        # right to left check each right sublist can be meet