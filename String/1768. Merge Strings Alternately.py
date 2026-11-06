class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i+=1

        # Python 的 Slicing（切片）不会因为 index 超出范围而报错，这和直接访问元素 word1[i] 不一样
        res.append(word1[i:])
        res.append(word2[i:])
        return "".join(res)

        # if len(word1) < len(word2):
        #     return "".join(res)+word2[i:]
        # elif len(word2) < len(word1):
        #     return "".join(res)+word1[i:]
        # else:
        #     return "".join(res)
        
        # Time complexity O(n)
        # Sapce complexity O(n)