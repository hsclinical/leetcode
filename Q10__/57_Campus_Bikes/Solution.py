class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        workerLen = len(workers)
        distToPair = {}
        for y, w in enumerate(workers):
            for x, b in enumerate(bikes):
                distance = abs(w[0] - b[0]) + abs(w[1] - b[1])
                if distance not in distToPair:
                    distToPair[ distance ] = []
                distToPair[ distance ].append( (y, x) )

        visitedW = set()
        visitedB = set()
        outcome = {}
        count = 0
        foundAll = False
        for distance in sorted(distToPair):
            pairs = sorted(distToPair[ distance ], key=lambda element: (element[0], element[1]))
            for pair in pairs:
                if pair[0] not in visitedW and pair[1] not in visitedB:
                    outcome[ pair[0] ] = pair[1]
                    visitedW.add( pair[0] )
                    visitedB.add( pair[1] )
                    count += 1
                    if count == workerLen:
                        foundAll = True
                        break
            if foundAll:
                break

        return [ outcome[x] for x in sorted(outcome) ]