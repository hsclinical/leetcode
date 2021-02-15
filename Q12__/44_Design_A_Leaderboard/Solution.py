import bisect

class Leaderboard:

    def __init__(self):
        self.scores = []
        self.idToScore = {}

    def addScore(self, playerId: int, score: int) -> None:
        previousScore = 0
        if playerId in self.idToScore:
            previousScore = self.idToScore[ playerId ]
            del self.scores[bisect.bisect_left(self.scores, previousScore)]
        self.idToScore[ playerId ] = score + previousScore
        bisect.insort(self.scores, score + previousScore)

    def top(self, K: int) -> int:
        if K >= len(self.scores):
            return sum(self.scores)
        else:
            return sum(self.scores[(-1)*K:])

    def reset(self, playerId: int) -> None:
        del self.scores[bisect.bisect_left(self.scores, self.idToScore[ playerId ])]
        del self.idToScore[ playerId ]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)