from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentenceLen = 0
        for word in sentence:
            sentenceLen += (len(word) + 1)
        if cols % sentenceLen == 0:
            return rows * (cols // sentenceLen)
        elif cols + 1 % sentenceLen == 0:
            return rows * ((cols + 1) // sentenceLen)
        else:
            numOfTimes = 0
            toExit = False
            curCol = 0
            curRow = 1
            while True:
                if (curCol != 0) and (curCol == cols or curCol == cols - 1) and (rows // curRow > 1):
                    repeatTimes = rows // curRow
                    curRow = curRow * repeatTimes
                    numOfTimes = numOfTimes * repeatTimes
                else:
                    if curCol == 0:
                        repeatTimes = (cols+1) // sentenceLen
                        if repeatTimes == 0:
                            newCol = curCol
                        else:
                            newCol = sentenceLen * repeatTimes - 1
                    else:
                        repeatTimes = (cols-curCol) // sentenceLen
                        newCol = sentenceLen * repeatTimes + curCol

                    numOfTimes += repeatTimes
                    curCol = newCol
                    toExit, newCol, addedRow = self.newRound(curCol, sentence, cols)
                    if toExit or curRow + addedRow > rows:
                        break
                    else:
                        numOfTimes += 1
                        curCol = newCol
                        curRow += addedRow

        return numOfTimes


    def newRound(self, curCol, sentence, cols):
        toExit = False
        addedRow = 0

        for word in sentence:
            wordLen = len(word)
            if wordLen > cols:
                # a single word is wider than the maximum cols allowed
                toExit = True
                break
            else:
                if curCol == 0:
                    # happen only when it's the initial word
                    curCol = wordLen
                else:
                    if curCol + wordLen + 1 > cols:
                        # next row
                        addedRow += 1
                        curCol = wordLen
                    else:
                        curCol = curCol + wordLen + 1

        return toExit, curCol, addedRow