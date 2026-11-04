class Solution:
    def generateParenthesis(self, n: int) -> list[str]:


        res = []
        path = []

        # Choices + Constraints:
        # 1. think about when we can add '('
        # 2. when can we add ')' 
        # my original solution is have a counter for '(', and make counter < n, and have a stack to store all added "(", if stack then could add ")"
        # logic can be simplified by below: have 2 counter
        # '(' : openN < n         (still have '(' available)
        # ')' : closeN < openN    (have unmatched '(')

        # Base case:
        # openN == closeN == n



        # The most important point for backtracking is that after finish when branch, undo the change for that branch!!!



        def backtrack(openN,closeN):
            if openN == closeN == n:
                res.append("".join(path))
                return 
            else:
                if openN < n:
                    path.append("(")
                    backtrack(openN+1,closeN)
                    path.pop()
                if closeN < openN:
                    path.append(")")
                    backtrack(openN,closeN+1)
                    path.pop()
        backtrack(0,0)

        return res