class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        for i in strs:
            i_s = "".join(sorted(i))
            if i_s not in word_dict.keys():
                word_dict[i_s] = [i]
            else:
                word_dict[i_s].append(i)
        
        return list(word_dict.values())

        # Set can not solve abbc and abcc problem 
        # set 会丢失长度信息
        # sort text = "".join(sorted(str))


        # optimal solution
        # 闭眼写出 defaultdict，干掉繁琐的 if/else
        word_dict = defaultdict(list)

        for word in strs:
            # 核心：生成绝对唯一的指纹作为 Key
            signature = "".join(sorted(word))
            word_dict[signature].append(word)

        return list(word_dict.values())