from typing import List

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        letterIndex = {}
        for i in range(len(S)):
            if S[i] not in letterIndex:
                letterIndex[ S[i] ] = []
            letterIndex[ S[i] ].append(i)

        trueCount = 0
        for word in words:
            letterMaxIndex = {}
            curWord = True
            lastIndex = -1
            for i in range(len(word)):
                # found novel letter which does not exist in S -> False
                if word[i] not in letterIndex:
                    curWord = False
                    break

                # may find the letter after current index
                found = False
                for j in range(len(letterIndex[ word[i] ])):
                    if letterIndex[ word[i] ][j] > lastIndex:
                        letterMaxIndex[ word[i] ] = j
                        lastIndex = letterIndex[ word[i] ][ j ]
                        found = True
                        break
                if not found:
                    curWord = False
                    break
            if curWord:
                trueCount += 1
        return trueCount
