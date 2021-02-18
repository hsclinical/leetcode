from typing import List

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        maxLen = len(A)
        count = {}
        if A[0] == B[0]:
            candidates = [ A[0] ]
            count[ A[0] ] = {}
            count[ A[0] ][ 0 ] = 1
            count[ A[0] ][ 1 ] = 1
        else:
            candidates = [ A[0], B[0] ]
            count[ A[0] ] = {}
            count[ A[0] ][ 0 ] = 1
            count[ A[0] ][ 1 ] = 0
            count[ B[0] ] = {}
            count[ B[0] ][ 0 ] = 0
            count[ B[0] ][ 1 ] = 1

        for i in range(1, maxLen):
            for j, candidate in enumerate(candidates):
                if candidate == A[i] and candidate == B[i]:
                    candidates = [ candidate ]
                    count[ A[i] ][ 0 ] += 1
                    count[ A[i] ][ 1 ] += 1
                    break
                elif candidate == A[i]:
                    count[ candidate ][ 0 ] += 1
                elif candidate == B[i]:
                    count[ candidate ][ 1 ] += 1
                else:
                    candidates[j] = 0
            candidates = [ x for x in candidates if x != 0 ]
            if len(candidates) == 0:
                return -1

        minSwitch = -1
        for candidate in candidates:
            num = min( maxLen - count[ candidate ][ 0 ], maxLen - count[ candidate ][ 1 ] )
            if minSwitch == -1 or minSwitch > num:
                minSwitch = num
        return minSwitch
