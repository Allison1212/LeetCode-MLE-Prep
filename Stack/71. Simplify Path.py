class Solution:
    def simplifyPath(self, path: str) -> str:
        # # My first version 
        # stack = list()
        # for s in path.split('/'):
        #     if s != '':
        #         if s != '/' and s != '.':
        #             if s == '..':
        #                 if stack:
        #                     stack.pop()
        #             else:
        #                 stack.append(s)
        
        # return "/"+"/".join(stack)

        # Imrovement 
        stack = list()
        for s in path.split('/'):
            if s == '..':
                if stack:
                    stack.pop()
            elif s != '.' and s:
                stack.append(s)
        
        return "/"+"/".join(stack)

        # Both time and space is O(N)
        # if s empty if s is False
