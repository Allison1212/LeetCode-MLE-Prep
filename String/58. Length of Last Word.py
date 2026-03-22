class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.strip().split(' ')
        print(s_list)
        return len(s_list[-1])
      