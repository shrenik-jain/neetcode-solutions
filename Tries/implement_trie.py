'''
Question: https://leetcode.com/problems/implement-trie-prefix-tree/
'''

class TrieNode:
    '''
    Create a TrieNode Class to store the Words in a Prefix Tree
    '''
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    '''
    The Prefix Tree which creates TrieNodes based on words and prefixes
    '''
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        # set `cur` to root (an empty TrieNode)
        cur = self.root

        # Iterate over all the characters in a word
        for c in word:
            # if character never appeared in the tree, create a new TrieNode for it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # The character appears in the tree, so move to that Node
            cur = cur.children[c]

        # after completing above loop, the word is complete, so mark the last character as endOfWord
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        # set `cur` to root (an empty TrieNode)
        cur = self.root

        # Iterate over all the characters in a word
        for c in word:
            # if the cbaracter does not appear in the Trie tree, then the word doesn't exist
            if c not in cur.children:
                return False
            # if above if block is skipped, means character does exist, so move to that Node
            cur = cur.children[c]

        # if all characters are found, check if last character is the endOfWord
        return cur.endOfWord


    def startsWith(self, prefix: str) -> bool:
        # set `cur` to root (an empty TrieNode)
        cur = self.root

        # Iterate over all the characters in a word
        for c in prefix:
            # if the cbaracter does not appear in the Trie tree, then the prefix doesn't exist
            if c not in cur.children:
                return False
            # if above if block is skipped, means character does exist, so move to that Node
            cur = cur.children[c]

        # if above loop is executed completely, we found the prefix
        # no need to check the endOfWord token, since it is a prefix, not a word
        return True
    

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)