class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_lst = list(pattern)
        s_lst = s.split()

        if len(p_lst) != len(s_lst):
            return False
        else:

            print(set(zip(p_lst,s_lst)))
            return len(set(p_lst)) == len(set(zip(p_lst,s_lst))) == len(set(s_lst))
        