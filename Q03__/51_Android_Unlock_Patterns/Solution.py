from typing import List
from functools import lru_cache

class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        if m > n:
            return 0
        else:
            cntList, combList = self.enumeratePath( n )
            return sum(cntList[(m-1):])

    @lru_cache(maxsize=None)
    def enumeratePath(self, n):
        if n == 1:
            outList = [ [i+1] for i in range(9) ]
            return( [ len(outList) ], outList )
        else:
            blockPairs = {}
            blockPairs[ (1, 3) ] = 2
            blockPairs[ (1, 7) ] = 4
            blockPairs[ (1, 9) ] = 5
            blockPairs[ (2, 8) ] = 5

            blockPairs[ (3, 7) ] = 5
            blockPairs[ (3, 9) ] = 6
            blockPairs[ (4, 6) ] = 5
            blockPairs[ (7, 9) ] = 8

            cntList, previousList = self.enumeratePath( n - 1 )
            currentList = []
            for previousSeq in previousList:
                for i in range(1, 10):
                    if i not in previousSeq:
                        # distinct
                        tmpList = [previousSeq[-1], i]
                        tmpList.sort()
                        tmpTuple = tuple(tmpList)
                        if tmpTuple not in blockPairs:
                            # OK
                            currentList.append( previousSeq[:] + [i] )
                        else:
                            if blockPairs[ tmpTuple ] in previousSeq:
                                # OK
                                currentList.append( previousSeq[:] + [i] )
            cntList.append( len(currentList) )
            return cntList, currentList



