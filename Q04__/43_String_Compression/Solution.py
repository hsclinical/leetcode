from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        charInfo = ''
        charCnt  = 0
        curIdx   = 0
        for char in chars:
            if charInfo == '':
                charInfo = char
                charCnt  = 1
            else:
                if char == charInfo:
                    charCnt += 1
                else:
                    if charCnt == 1:
                        chars[curIdx] = charInfo
                        curIdx += 1
                    else:
                        chars[curIdx] = charInfo
                        curIdx += 1
                        tmpString = str(charCnt)
                        for tmp in tmpString:
                            chars[curIdx] = tmp
                            curIdx += 1
                    charInfo = char
                    charCnt  = 1

        if charCnt == 1:
            chars[curIdx] = charInfo
            curIdx += 1
        else:
            chars[curIdx] = charInfo
            curIdx += 1
            tmpString = str(charCnt)
            for tmp in tmpString:
                chars[curIdx] = tmp
                curIdx += 1

        return curIdx