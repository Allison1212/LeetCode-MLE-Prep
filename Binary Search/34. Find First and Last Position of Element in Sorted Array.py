class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def bs(nums,lower_bound):
            l,r = 0,len(nums)-1
            i = -1

            while l <= r:
                mid = l + (r-l)//2

                if target < nums[mid]:
                    r = mid -1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    i = mid
                    if lower_bound:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i


        left = bs(nums,True)
        right = bs(nums,False)

        return [left,right]

        # Time complexity O(logn)
        # Space complexity O(1)







        # # brute force
        # left = 0 
        # right = len(nums)-1
        # lower = -1
        # upper = -1
        # while left <= right:
        #     if nums[left] == target and lower == -1:
        #         lower = left
        #         left+=1
        #     if nums[right] == target and upper == -1:
        #         upper = right
        #         right-=1
        #     if nums[left] < target:
        #         left +=1
        #     if nums[right] > target:
        #         right -=1
        # return [lower,upper]