class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        yDim = len(board)
        xDim = len(board[0])

        while True:
            # find positions may be eliminated
            # eliminate them and move top non-empty cell to bottom
            # repeat step 1 and 2 until there is no change any more

            # use DP to calculate values
            score = []
            cutoff = 3
            toUpdate = False
            # [h, v]
            # DP
            for y in range(yDim):
                newRow = []
                score.append(newRow)
                for x in range(xDim):
                    if x == 0:
                        score[y][x][0] = 1
                    else:
                        if board[y][x] == board[y][x-1]:
                            score[y][x][0] = score[y][x-1][0] + 1
                        else:
                            score[y][x][0] = 1

                    if y == 0:
                        score[y][x][1] = 1
                    else:
                        if board[y][x] == board[y-1][x]:
                            score[y][x][1] = score[y-1][x][1] + 1
                        else:
                            score[y][x][1] = 1

            # trace back and remove
            for y in reversed(range(yDim)):
                for x in reversed(range(xDim)):
                    if score[y][x][0] >= cutoff:
                        toUpdate = True
                        for i in range(1, score[y][x][0]):
                            board[y][x-i] = 0
                            score[y][x-i][0] = 0
                    if score[y][x][1] >= cutoff:
                        toUpdate = True
                        for i in range(score[y][x][1]):
                            board[y-i][x] = 0
                            score[y-i][x][1] = 0

            if toUpdate:
                # move cell down
                for x in range(xDim):
                    for y in range(yDim):

            else:
                break

        return board