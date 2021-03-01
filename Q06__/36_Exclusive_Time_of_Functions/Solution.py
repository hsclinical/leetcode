class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        outList = [ 0 ] * n
        stackFuncPoint = []
        stackTimePoint = []
        stackTimeExclude = []
        for i, singleLog in enumerate(logs):
            cell = singleLog.split(':')
            if len(stackFuncPoint) == 0:
                if cell[1] == 'end':
                    print("warning: (wrong begin) " + singleLog)
                stackFuncPoint.append( int(cell[0]) )
                stackTimePoint.append( int(cell[2]) )
                stackTimeExclude.append( 0 )
            else:
                if cell[1] == 'end':
                    if int(cell[0]) != stackFuncPoint[-1]:
                        print("warning: (func mismatch) " + singleLog)
                    funcId = int(cell[0])
                    stackFuncPoint.pop()
                    timeBgn = stackTimePoint.pop()
                    timeExc = stackTimeExclude.pop()
                    if len(stackTimeExclude) > 0:
                        stackTimeExclude[-1] += (int(cell[2]) - timeBgn + 1)
                    outList[ funcId ] += (int(cell[2]) - timeBgn + 1 - timeExc)
                else:
                    stackFuncPoint.append( int(cell[0]) )
                    stackTimePoint.append( int(cell[2]) )
                    stackTimeExclude.append( 0 )
        return outList