from typing import List

class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # convert string to number
        wordFreq = {}
        for word in words:
            freq = self.funcF(word)
            if freq not in wordFreq:
                wordFreq[ freq ] = 0
            wordFreq[ freq ] += 1

        # calculate accumulating value
        wordSum = {}
        curNum = 0
        reversedSort = sorted(wordFreq, reverse=True)
        reversedSortLen = len(reversedSort)
        for num in reversedSort:
            wordSum[ num ] = wordFreq[ num ] + curNum
            curNum += wordFreq[ num ]

        # scan queries
        outList = []
        for query in queries:
            queryNum = self.funcF(query)
            if queryNum in wordFreq:
                outList.append( wordSum[ queryNum ] - wordFreq[ queryNum ] )
            elif queryNum > reversedSort[0]:
                outList.append( 0 )
            elif queryNum < reversedSort[-1]:
                outList.append( wordSum[ reversedSort[-1] ] )
            else:
                outList.append( wordSum[ self.findCeiling(queryNum, reversedSort, 0, reversedSortLen-1) ] )
        return outList


    def funcF(self, s):
        smallestFreq = 0
        smallestChar = ''
        for i, char in enumerate(s):
            if i == 0:
                smallestFreq = 1
                smallestChar = char
            else:
                if char < smallestChar:
                    smallestFreq = 1
                    smallestChar = char
                elif char == smallestChar:
                    smallestFreq += 1
        return smallestFreq


    def findCeiling(self, num, numList, bgnIdx, endIdx):
        # num not in numList
        # numList is reverse sorted
        # num must be between numList[0] and numList[-1]
        if endIdx - bgnIdx == 1:
            return numList[bgnIdx]
        else:
            midIdx = (bgnIdx + endIdx) // 2
            if num < numList[midIdx]:
                return self.findCeiling(num, numList, midIdx, endIdx)
            else:
                return self.findCeiling(num, numList, bgnIdx, midIdx)

