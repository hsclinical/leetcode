class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # load board
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        letterX = {}
        letterY = {}
        for y in range(len(board)):
            for x in range(len(board[y])):
                letterX[ board[y][x] ] = x
                letterY[ board[y][x] ] = y

        # check input
        previousX = 0
        previousY = 0
        previousLetter = 'a'
        output = ""
        for i in range(len(target)):
            currentX = letterX[ target[i] ]
            currentY = letterY[ target[i] ]
            if previousLetter == 'z':
                if currentY > previousY:
                    output += 'D' * (currentY - previousY)
                elif currentY < previousY:
                    output += 'U' * (previousY - currentY)

                if currentX > previousX:
                    output += 'R' * (currentX - previousX)
                elif currentX < previousX:
                    output += 'L' * (previousX - currentX)
            else:
                if currentX > previousX:
                    output += 'R' * (currentX - previousX)
                elif currentX < previousX:
                    output += 'L' * (previousX - currentX)

                if currentY > previousY:
                    output += 'D' * (currentY - previousY)
                elif currentY < previousY:
                    output += 'U' * (previousY - currentY)

            output += '!'
            previousX = currentX
            previousY = currentY
            previousLetter = target[i]

        return output