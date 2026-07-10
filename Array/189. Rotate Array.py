class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # for i in range(k):
            
        #     nums[:] = [nums[-1]] + nums[:-1]
        #     print(nums[-1],nums[:-1])
        
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

        #.reverse() in place reverse
        # [::-1] create a new copy 
        # Rotate and Array = reverse the how array and reverse before k part and after k part