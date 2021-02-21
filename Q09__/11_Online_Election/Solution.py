import bisect
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.outcome = []

        freq = defaultdict(int)
        topFreq = 0
        for person in persons:
            freq[ person ] += 1
            if freq[ person ] > topFreq:
                topFreq = freq[ person ]
                self.outcome.append( person )
            elif freq[ person ] == topFreq:
                self.outcome.append( person )
            else:
                lastPerson = self.outcome[-1]
                self.outcome.append( lastPerson )


    def q(self, t: int) -> int:
        if t in self.times:
            idx = bisect.bisect_left(self.times, t)
            return self.outcome[idx]
        else:
            idx = bisect.bisect_left(self.times, t) - 1
            return self.outcome[idx]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)