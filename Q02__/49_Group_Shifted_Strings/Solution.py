from typing import List

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if len(strings) == 0:
            return []
        else:
            outDict = {}
            for singleString in strings:
                strLen = len(singleString)
                if strLen <= 1:
                    if strLen not in outDict:
                        outDict[ strLen ] = [ singleString ]
                    else:
                        outDict[ strLen ].append( singleString )
                else:
                    keyList = []
                    for i, char in enumerate(singleString):
                        if i == 0:
                            base = ord(singleString[i])
                        else:
                            keyList.append( (ord(singleString[i]) - base) % 26 )
                    keyTuple = tuple(keyList)
                    if keyTuple not in outDict:
                        outDict[ keyTuple ] = [ singleString ]
                    else:
                        outDict[ keyTuple ].append( singleString )

            outList = list( outDict.values() )
            return outList
