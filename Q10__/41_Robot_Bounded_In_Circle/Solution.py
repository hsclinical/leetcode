class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        destPosition, destDirection = self.oneStep(instructions)
        if destPosition[0] == 0 and destPosition[1] == 0:
            # return to (0, 0)
            return True
        else:
            if destDirection == 'N':
                return False
            else:
                return True

    def oneStep(self, instructions):
        curPosition = [0, 0]
        curDirection = 'N'
        changeDirt = {}
        changeDirt[ 'N' ] = { 'L' : 'W', 'R' : 'E' }
        changeDirt[ 'E' ] = { 'L' : 'N', 'R' : 'S' }
        changeDirt[ 'S' ] = { 'L' : 'E', 'R' : 'W' }
        changeDirt[ 'W' ] = { 'L' : 'S', 'R' : 'N' }
        for char in instructions:
            if char == 'L' or char == 'R':
                curDirection = changeDirt[ curDirection ][ char ]
            else:
                if curDirection == 'N':
                    curPosition[1] += 1
                elif curDirection == 'E':
                    curPosition[0] += 1
                elif curDirection == 'S':
                    curPosition[1] -= 1
                else:
                    curPosition[0] -= 1
        return curPosition, curDirection