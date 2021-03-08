# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        #curY = 499 # maxIdx = 998
        #curX = 499 # maxIdx = 998
        curCell = (499, 499)
        curStack = [ ]
        accessible = set()
        accessible.add( curCell )
        fChar = [ 'U','D','L','R' ]
        fCoord = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
        tbChar = { 'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L' }
        tbCoord  = { 'U': (1, 0), 'D': (-1, 0), 'L': (0, 1), 'R': (0, -1) }

        # visit all accessible cells
        foundTarget = False
        targetCell = None
        while True:
            if not foundTarget and master.isTarget():
                foundTarget = True
                targetCell = curCell

            foundNext = False
            for i, direction in enumerate(fChar):
                nextCell = (curCell[0] + fCoord[i][0], curCell[1] + fCoord[i][1])
                if master.canMove( direction ) and nextCell not in accessible:
                    # move
                    accessible.add( nextCell )
                    curStack.append( direction )
                    master.move( direction )
                    curCell = nextCell
                    foundNext = True
                    break

            if not foundNext:
                if len(curStack) == 0:
                    break
                else:
                    # move back
                    tracebackOne = curStack.pop()
                    master.move( tbChar[ tracebackOne ] )
                    nextCell = (curCell[0] + tbCoord[ tracebackOne ][0], curCell[1] + tbCoord[ tracebackOne ][1])
                    curCell = nextCell


        # find the shortest path
        if not foundTarget:
            return -1
        else:
            # bfs
            visited = set()
            curList = [ (499, 499) ]
            curStep = 0
            targetStep = 1
            found = False
            while True:
                nextList = []
                for curCell in curList:
                    for nextCoord in fCoord:
                        nextCell = (curCell[0] + nextCoord[0], curCell[1] + nextCoord[1])
                        if nextCell in accessible and nextCell not in visited:
                            visited.add( nextCell )
                            nextList.append( nextCell )
                            if nextCell == targetCell:
                                targetStep = curStep + 1
                                found = True
                                break
                if found:
                    break
                else:
                    curStep += 1
                    curList = nextList
            return targetStep
