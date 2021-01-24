from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.n = len(matrix)
        if self.n != 0:
            self.m = len(matrix[0])
        else:
            self.n = 0

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.n != 0:
            middleList = []
            for i in range(row1, row2+1):
                middleList.append(sum(self.matrix[i][col1:(col2+1)]))
            return(sum(middleList))
        else:
            return(0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
