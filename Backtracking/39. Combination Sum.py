class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        # # My first version
        # res = []
        # path = []

        # def backtrack(cum_sum,path):
        #     if cum_sum == target:
        #         sort_path = sorted(path)
        #         if sort_path not in res:
        #             res.append(sort_path)
        #         return
        #     for c in candidates:
        #         if cum_sum <= target:
        #             path.append(c)
        #             cum_sum += c
        #             backtrack(cum_sum,path)
        #             v = path.pop()
        #             cum_sum -= v
        
        # backtrack(0,path)
        # return res

        # # sorted(my_list) and my_list[::-1] not inplace sort 
        # # my_list.sort() in place sort, return null
        

        # Optimize
        res = []
        path = []

        def backtrack(start,cum_sum,path):
            if cum_sum == target:
                res.append(path.copy())
                return
            for i in range(start,len(candidates)):
                if cum_sum + candidates[i] <= target:
                    path.append(candidates[i])
                    backtrack(i,cum_sum + candidates[i],path)
                    path.pop()
        
        backtrack(0,0,path)
        return res

        # 通过只看>= 当前数字的 数字这样避免 223， 322 这种重复
        # time complexity:
            # n = len(candidates)、D = target // min(candidates)、R = 有效组合数量
            # search: D 为 最大层数， 每一层最多search n candidates， 所以 每次recursive n^D, for loop n cadiates, so n * n^D -> n^(D+1)
            # save the path: path 最长D, 然后* 有效组合R
            #--> n^(D+1) + DR
        # space complexity O(n)
        # Auxiliary Space: O(D)
        # - Recursion stack: O(D)
        # - Shared path: O(D)

        # Output Space: O(D * R)
        # Total Space: O(D + D * R)
