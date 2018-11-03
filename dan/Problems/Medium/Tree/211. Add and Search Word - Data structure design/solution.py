class TrieNode():
    def __init__(self, val):
        self.links = [None] * 26
        self.isEnd = False
        self.val = val
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode(-1)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for l in word:
            if not node.links[ord(l) - ord('a')]:
                node.links[ord(l) - ord('a')] = TrieNode(l)
            node = node.links[ord(l) - ord('a')]
        node.isEnd = True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(word, self.trie)
        
    def match(self, string, node):
        if len(string) == 0:
            return node.isEnd
        l = string[0]
        if not l == ".":
            nxt = node.links[ord(l) - ord('a')]
            if nxt:
                return self.match(string[1:], nxt)
            return False
        else:
            for nxt in node.links:
                if nxt:
                    if self.match(string[1:], nxt):
                        return True
            return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
