class Solution:
    def isValid(self, s: str) -> bool:
        
        # # My solution
        # map_dic = {
        #     '(':')',
        #     '{': '}',
        #     '[':']'
        # }
        # stack = deque()
        # for i in range(len(s)):
        #     if s[i] not in map_dic and stack:
        #         last_value = stack.pop()
        #         if map_dic.get(last_value) != s[i]:
        #             stack.append(last_value)
        #             stack.append(s[i])
        #     else:
        #         stack.append(s[i])
            
        # return len(stack) == 0

        # Better solution
        # python list is faster then deque()
        # for i in s is better then for i in range(len(s))
        # Retur early 
        map_dic = {
            '(':')',
            '{': '}',
            '[':']'
        }
        stack = []
        for i in s:
            if i in map_dic:
                stack.append(i)
            else:
                if not stack:
                    return False
                if map_dic.get(stack.pop()) != i:
                    return False
            
        return len(stack) == 0
            

