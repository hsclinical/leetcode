class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T) == 0:
            return []
        elif len(T) == 1:
            return [ 0 ]
        else:
            stackTmp = []
            stackIdx = []
            daysToWait = {}
            for i, t in enumerate(T):
                if i == 0:
                    stackTmp.append(t)
                    stackIdx.append(i)
                else:
                    while True:
                        if len(stackTmp) == 0 or stackTmp[-1] >= t:
                            stackTmp.append(t)
                            stackIdx.append(i)
                            break
                        else:
                            lastTmp = stackTmp.pop()
                            lastIdx = stackIdx.pop()
                            daysToWait[ lastIdx ] = i - lastIdx

            for idx in stackIdx:
                daysToWait[ idx ] = 0
            outcome = [ daysToWait[x] for x in sorted(daysToWait.keys()) ]

            return outcome