class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s) <= 1:
            return s
        else:
            charToPos = {}
            for i, char in enumerate(s):
                if char not in charToPos:
                    charToPos[ char ] = []
                charToPos[ char ].append( i )

            outcome = ''
            sortedCharList = sorted( charToPos.keys() )
            charCondition = {}
            while True:
                if len(sortedCharList) == 1:
                    outcome += sortedCharList[0]
                    break
                nextChar = self.findNextLetter(charToPos, sortedCharList, charCondition)
                if nextChar != None:
                    outcome += nextChar
            return outcome

    def findNextLetter(self, charToPos, sortedCharList, charCondition):
        curChar = sortedCharList[0]
        curLowestPos = charToPos[ curChar ][ 0 ]
        for i, char in enumerate(sortedCharList):
            if char not in charCondition or charCondition[ char ] not in charToPos:
                curChar = char
                curLowestPos = charToPos[ curChar ][ 0 ]
                break

        found = True
        for char in reversed(sortedCharList):
            if char == curChar:
                pass
            else:
                checkLargestPos = charToPos[ char ][ -1 ]
                if curLowestPos > checkLargestPos:
                    charCondition[ curChar ] = char
                    found = False
                    break
        if found:
            num = charToPos[ curChar ][ 0 ]
            del charToPos[ curChar ]
            sortedCharList.remove( curChar )
            for i, char in enumerate(sortedCharList):
                charToPos[ char ] = [i for i in charToPos[ char ] if i > num]
            return curChar
        else:
            return None

