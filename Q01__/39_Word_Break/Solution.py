from typing import List
import re

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        setA = set(s)

        letterCount = {}
        letterWord = {}
        filterWordDict = []
        for wd in wordDict:
            setWord = set(wd)
            if len(setWord - setA) > 0:
                pass
            else:
                filterWordDict.append(wd)
                for letter in setWord:
                    if letter in letterCount:
                        letterCount[letter] += 1
                        letterWord[letter].add( wd )
                    else:
                        letterCount[letter] = 1
                        letterWord[letter] = set()
                        letterWord[letter].add( wd )

        output = True
        setB = set(''.join(filterWordDict))
        if len(setA - setB) != 0:
            output = False
        else:
            uniqSet = set()
            for letter in letterCount:
                if letterCount[letter] == 1:
                    uniqSet.update(letterWord[letter])

            for word in uniqSet:
                if s.find(word) == -1:
                    output = False
                    break

            if output:
                if len(uniqSet) == 0:
                    sList = [ s ]
                else:
                    sList = re.split('|'.join(uniqSet), s)
                for sSingle in sList:
                    if sSingle != "":
                        if not self.recursiveCheck(sSingle, filterWordDict):
                            output = False
                            break

        return output

    def recursiveCheck(self, s: str, wordDict: List[str]) -> bool:
        output = False
        for wd in wordDict:
            if s == wd:
                output = True
                break
            elif s.startswith(wd):
                child = self.recursiveCheck(s[len(wd):], wordDict)
                if child == True:
                    output = True
                    break

        return output
