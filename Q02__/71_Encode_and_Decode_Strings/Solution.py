from typing import List

class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        outString = ''
        unitLen = 8
        for singleStr in strs:
            strLen = len(singleStr)
            strLenLen = len(str(strLen))
            outString += ('0' * ( unitLen - strLenLen )) + str(strLen)
            outString += singleStr
        return(outString)

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        strList = []
        inputLen = len(s)
        if inputLen > 0:
            unitLen = 8
            curIdx = 0
            while True:
                strLen = int(s[curIdx:(curIdx+unitLen)])
                if strLen == 0:
                    strList.append('')
                    curIdx = curIdx+unitLen
                else:
                    singleS = s[(curIdx+unitLen):(curIdx+unitLen+strLen)]
                    strList.append(singleS)
                    curIdx = curIdx+unitLen+strLen
                if curIdx >= inputLen:
                    break
        return(strList)




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))