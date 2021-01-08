from typing import List

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        longestLen = 0
        maxScore = {}
        numCount = {}
        for i, num in enumerate(A):
            if i == 0:
                maxScore[ A[i] ] = {}
                numCount[ A[i] ] = 1
            else:
                if A[i] not in numCount:
                    numCount[ A[i] ] = 1
                else:
                    numCount[ A[i] ] += 1
                if numCount[ A[i] ] > longestLen:
                    longestLen = numCount[ A[i] ]

                if A[i] not in maxScore:
                    maxScore[ A[i] ] = {}
                for j in reversed(range(i)):
                    diff = A[i] - A[j]
                    if diff != 0:
                        if diff in maxScore[ A[j] ]:
                            if diff in maxScore[ A[i] ] and maxScore[ A[i] ][ diff ] >= maxScore[ A[j] ][ diff ] + 1:
                                pass
                            else:
                                maxScore[ A[i] ][ diff ] = maxScore[ A[j] ][ diff ] + 1
                        else:
                            maxScore[ A[i] ][ diff ] = 2
                        if maxScore[ A[i] ][ diff ] > longestLen:
                            longestLen = maxScore[ A[i] ][ diff ]

        return longestLen
