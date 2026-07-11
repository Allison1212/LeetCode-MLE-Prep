class Solution:
    def jump(self, nums: List[int]) -> int:
        n = f = step = 0

        while f < len(nums) -1:
            farest = 0
            for v in range(n,f+1):
                farest = max(farest, v + nums[v])
            n = f + 1
            f = farest 
            step += 1
        return step

        # BFS-> 1D array sliding window, we only car two point what the start and end of the window