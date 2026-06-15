class Solution:
    def reverseVowels(self, s: str) -> str:
        v_list= ['a','e','i','o','u']
        # string can not inplace the change use index so we need to convert it to list
        s_list = list(s)
        left = 0
        right = len(s) - 1
        left_w = s_list[left]
        right_w = s_list[right]  

        while right > left:
            if left_w.lower() in v_list:
                if right_w.lower() in v_list:
                    s_list[left] = right_w
                    s_list[right] = left_w
                    right = right -1
                    left = left + 1

                    right_w = s_list[right]
                    left_w = s_list[left] 
                else:
                    right = right - 1
                    right_w = s_list[right] 
            else:
                left = left + 1
                left_w = s_list[left]
        return "".join(s_list)


        