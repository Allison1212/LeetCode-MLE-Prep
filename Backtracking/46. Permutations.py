class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        res = []

        path = []

        def backtrack(i,path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            else:
                for i in range(len(nums)):
                    if nums[i] not in path:
                        path.append(nums[i])
                        backtrack(i+1,path)
                        path.pop()
        
        backtrack(0,[])

        return res