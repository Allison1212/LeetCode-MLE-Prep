class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiou')
        left = 0
        right = len(s) - 1
        s_list = list(s)

        while left < right:
            if s_list[left].lower() not in vowels:
                left+=1
            elif s_list[right].lower() not in vowels:
                right-=1
            else:
                left_l = s_list[left]
                s_list[left] = s_list[right]
                s_list[right] = left_l
                left +=1
                right-=1
                    
        return "".join(s_list)

        # Time complexity O(n)
        # Space complexity O(n)
        # string to list of letter use list(string)
        # string to set of unique characters use set(string)


        