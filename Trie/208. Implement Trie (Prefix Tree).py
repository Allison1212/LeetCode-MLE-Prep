class TrieNode:

    def __init__(self):
        self.children = {}
        self.endofword = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True


        

    def search(self, word: str) -> bool:
        
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.endofword
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

    # Timecomplexity = O(L)
    # Spacecomplexity = O(L)
    # L 是word or prefix 的长度
    # 这题的gap 是我想到了用一个node 一个node 接，但我不会写trie node， 不了解trie 这个data structure

#     # brute force
#     def __init__(self):
#         self.prefix_dict = dict()
#         self.trie_list = list()

#     def insert(self, word: str) -> None:
#         self.trie_list.append(word)

#         for i in range(1,len(word)+1):
#             if word[:i] not in self.prefix_dict:
#                 self.prefix_dict[word[:i]] = [word]
#             else:
#                 self.prefix_dict[word[:i]].append(word)

        

#     def search(self, word: str) -> bool:
#         return word in self.trie_list
        

#     def startsWith(self, prefix: str) -> bool:
#         return prefix in self.prefix_dict
        


# # Your Trie object will be instantiated and called as such:
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)