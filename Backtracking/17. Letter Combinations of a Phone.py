class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        numToStr = {
            '2':['a','b','c'],
            '3': ['d','e','f'],
            '4':['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8':['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        # Recursive 
        # res = []
     
        # def backtrack(i,curr_str):
        #     if i>= len(digits):
        #         res.append(curr_str)
        #         return
        #     for c in numToStr[digits[i]]:
        #         backtrack(i+1,curr_str+c)

        # if digits:
        #     backtrack(0,'')

        # return res

        # # Time complexity O(4^n)
        # # Space complexity: O(n^2): curr_str+c create new string, it will save, a, ad, adg


        # Path pop and append

        res = []

        def backtrack(i,path):
            if len(path) == len(digits):
                res.append("".join(path))
                return 
            for c in numToStr[digits[i]]:
                path.append(c)
                backtrack(i+1,path)
                path.pop()
        
        if digits:
            backtrack(0,[])
        return res
         # Time complexity O(4^n)
         # Space complexity: O(n4^n): Stores up to 4ⁿ strings, each of length n
         # Backtrack 题想明白base case 是什么，然后recursion case 是什么

                