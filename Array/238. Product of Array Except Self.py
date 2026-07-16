class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Use division not allowed 
        # prod = 1
        # zero = 0
        # for i in nums:
        #     if i != 0:
        #         prod = prod * i
        #     else:
        #         zero+=1

        # if zero > 1:
        #     return [0]*len(nums)
        # else:
        #     if zero == 1:
        #         return [prod if x == 0 else 0 for x in nums]
        #     else:
        #         return [int(x / y) for x, y in zip([prod]*len(nums), nums)]


        # Prefix and post fix, and result list not count in to extra space 
        res = [1]
        for i in range(len(nums)-1):
            new = res[-1] * nums[i]
            res.append(new)

        h = len(nums) -1
        prod = 1
        while h >= 0:
            res[h] = res[h] * prod
            prod = prod * nums[h]
            h-=1
        return res

        ### After clean up (optimize code)
        # Pre-allocate the array with 1s so we don't have to use .append()
        n = len(nums)
        res = [1]*n
        # 1. Forward Pass: Calculate prefixes
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]

        prod = 1
        # 2. Backward Pass: Multiply by suffixes
        # range(start,end,step),end -1, last number is 0
        for i in range(n-1,-1,-1):
            res[i] *= prod 
            prod *= nums[i]
        return res