class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n cannot be 0. if n == 0, times.length == 0 as well. different from the condition provided

        timeToSpend = {}
        for singleTime in times:
            if singleTime[0] not in timeToSpend:
                timeToSpend[ singleTime[0] ] = {}
            timeToSpend[ singleTime[0] ][ singleTime[1] ] = singleTime[2]

        confirmed = {}
        visited = {}

        confirmed[ k ] = 0
        if k in timeToSpend:
            for nextNode in timeToSpend[ k ]:
                visited[ nextNode ] = timeToSpend[ k ][ nextNode ]

        while True:
            if len(visited) == 0:
                break
            else:
                curNodes = [ i for i in visited if visited[i] == min(visited.values()) ]
                for curNode in curNodes:
                    if curNode in timeToSpend:
                        for nextNode in timeToSpend[ curNode ]:
                            if nextNode not in confirmed:
                                maxVal = timeToSpend[ curNode ][ nextNode ] + visited[ curNode ]
                                if nextNode not in visited or visited[ nextNode ] > maxVal:
                                    visited[ nextNode ] = maxVal

                    confirmed[ curNode ] = visited[ curNode ]
                    del visited[ curNode ]

        maxTime = 0
        allVisited = True
        for i in range(1, n+1):
            if i not in confirmed:
                allVisited = False
                break
            else:
                if confirmed[ i ] > maxTime:
                    maxTime = confirmed[ i ]

        if allVisited:
            return maxTime
        else:
            return -1
