from typing import List

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 0:
            return None
        elif n == 0:
            return 1
        elif n < 4:
            return n
        else:
            squares = []
            initNum = 2
            while True:
                perfectSquare = initNum ** 2
                if perfectSquare < n:
                    squares.append( perfectSquare )
                    initNum += 1
                elif perfectSquare == n:
                    return 1
                else:
                    break

            matrix = [i for i in range(n+1)]
            for i, square in enumerate(squares):
                for j in range(square, n+1):
                    matrix[j] = min(matrix[j-square] + 1, matrix[j])

            return matrix[n]
