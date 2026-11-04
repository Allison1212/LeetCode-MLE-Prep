class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(j,path): 
            if len(path) == k:
                res.append(path.copy())
                return 
            for i in range(j,n+1):
                path.append(i)
                backtrack(i+1,path)
                path.pop()

        
        backtrack(1,[])
        return res

        # time complexity : O(n^2)
        # space complexity : O()