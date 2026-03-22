# Time Complexity: O(m + n) where m = len(ransomNote) and n = len(magazine).
# Space Complexity: O(k) where k is the number of distinct characters stored in the
# hash map (at most constant 26 for lowercase letters).
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        flag = True
        m_dict = {}
        for l in magazine:
            if l in m_dict:
                m_dict[l] = m_dict.get(l) + 1
            else:
                m_dict[l] = 1

        print(m_dict)
        for i in ransomNote:
            if m_dict.get(i):
                m_dict[i] = m_dict.get(i) - 1
                if m_dict.get(i) < 0:
                    flag = False
            else:
                flag = False

        return flag
        
