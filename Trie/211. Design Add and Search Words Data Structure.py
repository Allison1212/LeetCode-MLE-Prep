
class Trie_Node:
    def __init__(self):
        self.children = {}
        self.endofword = False



class WordDictionary:

    def __init__(self):
        self.root = Trie_Node()
    

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie_Node()
            curr = curr.children[c]
            
        curr.endofword = True
        

    

    # Use DFS to search for each child when meet special case
    def search(self, word: str) -> bool:
        def dfs(node,j):
            
            curr = node
            for i in range(j,len(word)):
                c = word[i]
                if c == '.':
                    for children in curr.children.values():
                        if dfs(children,i+1):
                            return True
                    return False

                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c] 
            
            return curr.endofword

        return dfs(self.root,0)

# search:
# Time complexity O(26^L), L is the length of word
# Space complexity O(L)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)