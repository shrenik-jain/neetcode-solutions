'''
Question: https://leetcode.com/problems/design-add-and-search-words-data-structure/
'''


class TrieNode:

    def __init__(self):
        self.children = {} # {a: TrieNode()}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)
    
    def dfs(self, j, root, word) -> bool:
        cur = root

        for i in range(j, len(word)):
            c = word[i]

            if c == ".":
                for child in cur.children.values():
                    if self.dfs(i + 1, child, word):
                        return True

                return False

            else:
                if c not in cur.children:
                    return False
                cur = cur.children[c]

        return cur.endOfWord


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)