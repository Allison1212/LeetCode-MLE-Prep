class Solution:
    def climbStairs(self, n: int) -> int:

        # step n = step n-1 + step n-2

        # Recursive intuitive but out of time limited 
        # if n == 1:
        #     return 1
        # elif n == 2:
        #     return 2
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        
        if n <= 2:
            return n
        
        onestep = 2
        twostep = 1

        i = 3
        while i <= n:
            current = onestep + twostep

            twostep = onestep
            onestep = current
            i+=1
            
        
        return current

        # DP: solve problem by solving subproblem
        