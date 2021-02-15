from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[ word ] += 1
        sortedList = sorted(freq.items(), key=lambda x: (-x[1], x[0]), reverse=True)
        return reversed([ x[0] for x in sortedList[-k:] ])

