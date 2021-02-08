import re

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordSet = []
        self.searchResult = {}
        self.wordSearched = {}

    def addWord(self, word: str) -> None:
        self.wordSet.append( word )

    def search(self, word: str) -> bool:
        if word in self.searchResult and self.searchResult[ word ]:
            # searched before and found
            return True
        else:
            regex = re.compile("^"+word+"$")
            if word in self.searchResult:
                # searched before, but never found
                lastIdx = self.wordSearched[ word ]
                matches = [str for str in self.wordSet[lastIdx: ] if re.match(regex, str)]
            else:
                # never search before
                matches = [str for str in self.wordSet if re.match(regex, str)]
            self.wordSearched[ word ] = len( self.wordSet )

            if len(matches) == 0:
                self.searchResult[ word ] = False
                return False
            else:
                return True
                self.searchResult[ word ] = True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)