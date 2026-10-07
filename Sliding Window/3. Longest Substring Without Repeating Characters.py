class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # # My solution
        # val_i = dict()

        # left = 0
        # right = 0

        # max_length = 0
        # if len(s) == 1:
        #     return 1

        # while right < len(s):
            
        #     if s[right] in val_i.keys():
        #         max_length = max(max_length,right-left)
        #         left = max(left, val_i[s[right]] + 1)
        #         if right - val_i[s[right]] == 1:
        #             val_i = dict()
        #         val_i[s[right]] = right
        #     else:
        #         val_i[s[right]] = right
        #     right+=1
        # return max(max_length,right-left)

        # optimize version
        val_i = dict()

        left = 0
        right = 0

        max_length = 0

        while right < len(s):
            char = s[right]
            if char in val_i.keys():
                left = max(left, val_i[char] + 1)
            val_i[char] = right
            max_length = max(max_length,right-left + 1)
            right+=1
        return max_length

        # Using set to track characters in the current window
        left = right = 0
        res = 0
        seen = set()

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            
            seen.add(s[right])
            res = max(res, right - left + 1)
            right +=1
        return res
        # 这里我的差距是没想到用set, 当不看顺序，看有没有就要想到set
        # slide window
        # 用while 处理duplication
        