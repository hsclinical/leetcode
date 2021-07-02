class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1Len = len(text1) + 1
        text2Len = len(text2) + 1
        maxScore = 0
        matrix = [ [0] * text1Len for i in range(text2Len) ]
        for x in range(1, text1Len):
            for y in range(1, text2Len):
                if text1[x-1] == text2[y-1]:
                    singleValue = 1
                else:
                    singleValue = 0
                matrix[y][x] = max( matrix[y-1][x-1] + singleValue, matrix[y-1][x], matrix[y][x-1] )
                if matrix[y][x] > maxScore:
                    maxScore = matrix[y][x]
        return maxScore
