class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False
        else: 
            s_i = 0
            t_i = 0
            while (s_i < len(s)) and (t_i < len(t)):
                print(s_i,t_i)
                if s[s_i] == t[t_i]:
                    s_i = s_i + 1
                    t_i = t_i + 1
                else:
                    t_i = t_i + 1
                    if t_i == len(t):
                        return False
            return s_i == len(s)

# Two Pointer, only one for loop, no need second loop