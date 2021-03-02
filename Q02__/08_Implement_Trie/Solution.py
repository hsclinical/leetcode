class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.append( word )

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.words:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        subWords = [ x for x in self.words if x.startswith(prefix) ]
        if len(subWords) == 0:
            return False
        else:
            return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)