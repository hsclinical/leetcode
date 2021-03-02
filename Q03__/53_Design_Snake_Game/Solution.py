class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.yLen = height
        self.xLen = width
        self.food = food
        self.curPos = (0, 0)
        self.curIdx = 0
        self.curPath = [ (0, 0) ]
        self.gameOver = False

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        if self.gameOver:
            return -1

        if direction == 'U':
            nextY = self.curPos[0] - 1
            nextX = self.curPos[1]
        elif direction == 'D':
            nextY = self.curPos[0] + 1
            nextX = self.curPos[1]
        elif direction == 'L':
            nextY = self.curPos[0]
            nextX = self.curPos[1] - 1
        elif direction == 'R':
            nextY = self.curPos[0]
            nextX = self.curPos[1] + 1
        else:
            print("Error input ( " + direction + " )." )

        if nextY >= 0 and nextY < self.yLen and nextX >= 0 and nextX < self.xLen and (nextY, nextX) not in self.curPath[1:]:
            if self.curIdx < len(self.food) and nextY == self.food[self.curIdx][0] and nextX == self.food[self.curIdx][1]:
                self.curPath.append( (nextY, nextX) )
                self.curIdx += 1
            else:
                self.curPath.append( (nextY, nextX) )
                self.curPath.pop(0)
            self.curPos = (nextY, nextX)
            return self.curIdx
        else:
            # end
            self.gameOver = True
            return -1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)