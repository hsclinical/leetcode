from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        lenToWord = {}
        score = {}
        for word in words:
            # remove duplicate word
            if word not in score:
                score[ word ] = 1

                # group word by length
                curLen = len(word)
                if curLen not in lenToWord:
                    lenToWord[ curLen ] = []
                lenToWord[ curLen ].append( word )

        longestLen = 1
        # sort the word length from smallest to largest
        sortedLenList = sorted(lenToWord.keys())
        for i in range(len(sortedLenList)):
            if i == 0 or sortedLenList[i] - sortedLenList[i-1] > 1:
                pass
            else:
                # check any combination between i and i-1
                for curWord in lenToWord[ sortedLenList[i] ]:
                    for preWord in lenToWord[ sortedLenList[i-1] ]:
                        if self.isPredecessor(curWord, preWord):
                            if score[ curWord ] < score[ preWord ] + 1:
                                score[ curWord ] = score[ preWord ] + 1
                                if score[ curWord ] > longestLen:
                                    longestLen = score[ curWord ]
        return longestLen

    def isPredecessor(self, curWord, preWord):
        mismatch = 0
        returnVal = True
        for i in range(len(preWord)):
            if preWord[i] == curWord[i + mismatch]:
                pass
            else:
                mismatch += 1
                if mismatch >= 2 or preWord[i] != curWord[i + mismatch]:
                    returnVal = False
                    break
        return returnVal
