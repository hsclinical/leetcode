from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.xMaxIdx = len(heights[0])-1
        self.yMaxIdx = len(heights)-1
        bgnCell = (0, 0)
        endCell = (self.xMaxIdx, self.yMaxIdx)
        self.visited = {}
        self.border = {}
        self.border[ bgnCell ] = 0
        output = -1

        #print(heights)
        while True:
            #print("IV", self.visited)
            #print("IB", self.border)
            keyWithMinVal = min(self.border, key=self.border.get)
            if keyWithMinVal == endCell:
                output = self.border[ keyWithMinVal ]
                break
            else:
                # add this cell to visited
                self.visited[ keyWithMinVal ] = self.border[ keyWithMinVal ]

                # remove this cell from border
                del self.border[ keyWithMinVal ]

                # find adjacent cells and val that not in visited
                # check (keyWithMinVal[0], keyWithMinVal[1]-1)
                if keyWithMinVal[1]-1 >= 0 and keyWithMinVal[1]-1 <= self.yMaxIdx and (keyWithMinVal[0], keyWithMinVal[1]-1) not in self.visited:
                    self.checkCell(keyWithMinVal[0], keyWithMinVal[1]-1, heights)

                # check (keyWithMinVal[0], keyWithMinVal[1]+1)
                if keyWithMinVal[1]+1 >= 0 and keyWithMinVal[1]+1 <= self.yMaxIdx and (keyWithMinVal[0], keyWithMinVal[1]+1) not in self.visited:
                    self.checkCell(keyWithMinVal[0], keyWithMinVal[1]+1, heights)

                # check (keyWithMinVal[0]-1, keyWithMinVal[1])
                if keyWithMinVal[0]-1 >= 0 and keyWithMinVal[0]-1 <= self.xMaxIdx and (keyWithMinVal[0]-1, keyWithMinVal[1]) not in self.visited:
                    self.checkCell(keyWithMinVal[0]-1, keyWithMinVal[1], heights)

                # check (keyWithMinVal[0]+1, keyWithMinVal[1])
                if keyWithMinVal[0]+1 >= 0 and keyWithMinVal[0]+1 <= self.xMaxIdx and (keyWithMinVal[0]+1, keyWithMinVal[1]) not in self.visited:
                    self.checkCell(keyWithMinVal[0]+1, keyWithMinVal[1], heights)
            #print("OV", self.visited)
            #print("OB", self.border)
            #print("\n")
        return output

    def checkCell(self, xIdx, yIdx, heights):
        if xIdx-1 >= 0 and xIdx-1 <= self.xMaxIdx and (xIdx-1, yIdx) in self.visited:
            val_1 = abs(heights[yIdx][xIdx] - heights[yIdx][xIdx-1])
            val_2 = self.visited[ (xIdx-1, yIdx) ]
            if val_1 > val_2:
                val_3 = val_1
            else:
                val_3 = val_2
            if (xIdx, yIdx) in self.border and self.border[ (xIdx, yIdx) ] < val_3:
                pass
            else:
                self.border[ (xIdx, yIdx) ] = val_3
            #print("A1", val_1, val_2, val_3, self.border[ (xIdx, yIdx) ])
        if xIdx+1 >= 0 and xIdx+1 <= self.xMaxIdx and (xIdx+1, yIdx) in self.visited:
            val_1 = abs(heights[yIdx][xIdx] - heights[yIdx][xIdx+1])
            val_2 = self.visited[ (xIdx+1, yIdx) ]
            if val_1 > val_2:
                val_3 = val_1
            else:
                val_3 = val_2
            if (xIdx, yIdx) in self.border and self.border[ (xIdx, yIdx) ] < val_3:
                pass
            else:
                self.border[ (xIdx, yIdx) ] = val_3
            #print("A2", val_1, val_2, val_3, self.border[ (xIdx, yIdx) ])
        if yIdx-1 >= 0 and yIdx-1 <= self.yMaxIdx and (xIdx, yIdx-1) in self.visited:
            val_1 = abs(heights[yIdx][xIdx] - heights[yIdx-1][xIdx])
            val_2 = self.visited[ (xIdx, yIdx-1) ]
            if val_1 > val_2:
                val_3 = val_1
            else:
                val_3 = val_2
            if (xIdx, yIdx) in self.border and self.border[ (xIdx, yIdx) ] < val_3:
                pass
            else:
                self.border[ (xIdx, yIdx) ] = val_3
            #print("A3", val_1, val_2, val_3, self.border[ (xIdx, yIdx) ])
        if yIdx+1 >= 0 and yIdx+1 <= self.yMaxIdx and (xIdx, yIdx+1) in self.visited:
            val_1 = abs(heights[yIdx][xIdx] - heights[yIdx+1][xIdx])
            val_2 = self.visited[ (xIdx, yIdx+1) ]
            if val_1 > val_2:
                val_3 = val_1
            else:
                val_3 = val_2
            if (xIdx, yIdx) in self.border and self.border[ (xIdx, yIdx) ] < val_3:
                pass
            else:
                self.border[ (xIdx, yIdx) ] = val_3
            #print("A4", val_1, val_2, val_3, self.border[ (xIdx, yIdx) ])
