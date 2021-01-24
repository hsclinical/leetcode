from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # len(workers) <= len(bikes)
        N = len(workers)
        M = len(bikes)
        distMatrix = [ [0] * M for _ in range(N) ]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distMatrix[i][j] = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

        print(distMatrix)

        Vdist = {}
        Vdist[ 0 ] = 0
        Udist = {}
        stopNode = 0
        for i in range(N):
            stopNode = stopNode | 1 << i

        # need track which bike-worker pair contribute to this value
        bikeSet = {}
        bikeSet[ 0 ] = set()
        while True:
            # find the next node to add
            for curNode in Vdist:
                for i in range(N):
                    nextNode = curNode | 1 << i
                    if nextNode not in Vdist:
                        initFlag = True
                        for j, singleDist in enumerate(distMatrix[i]):
                            if j not in bikeSet[ curNode ]:
                                if initFlag:
                                    thisDist = singleDist
                                    bikeIdx = j
                                    initFlag = False
                                else:
                                    if singleDist < thisDist:
                                        thisDist = singleDist
                                        bikeIdx = j
                        if nextNode not in Udist or Udist[ nextNode ] > Vdist[ curNode ] + thisDist:
                            Udist[ nextNode ] = Vdist[ curNode ] + thisDist
                            bikeSet[ nextNode ] = bikeSet[ curNode ].copy()
                            bikeSet[ nextNode ].add( bikeIdx )

            # find the smallest value in Udist
            added = min(Udist, key=Udist.get)
            Vdist[ added ] = Udist[ added ]
            del Udist[ added ]

            # exist the loop
            if added == stopNode:
                break

        return Vdist[ stopNode ]