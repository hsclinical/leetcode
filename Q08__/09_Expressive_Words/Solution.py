from typing import List

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        numExtent = 0
        (sLetter, sCount) = self.wordToCount(S)
        sString = ''.join(sLetter)
        for word in words:
            (wLetter, wCount) = self.wordToCount(word)
            wString = ''.join(wLetter)
            if sString == wString:
                #print(word)
                passFilter = True
                for i in range(len(sCount)):
                    if sCount[i] == wCount[i]:
                        pass
                    elif sCount[i] < wCount[i]:
                        passFilter = False
                        break
                    else:
                        if sCount[i] < 3:
                            passFilter = False
                            break
                if passFilter:
                    #print("  " + word)
                    numExtent += 1
        return numExtent

    def wordToCount(self, word):
        letterList = []
        countList = []
        previousLetter = ""
        count = 0
        for letter in word:
            if previousLetter == "":
                previousLetter = letter
                count = 1
            else:
                if letter == previousLetter:
                    count += 1
                else:
                    letterList.append(previousLetter)
                    countList.append(count)
                    previousLetter = letter
                    count = 1
        letterList.append(previousLetter)
        countList.append(count)
        return(letterList, countList)
