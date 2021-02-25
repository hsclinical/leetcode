from typing import List
from collections import defaultdict

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        longestLen = 0

        freq = defaultdict(int)
        maxType = 2
        idxBgn = 0
        for i, singleTree in enumerate(tree):
            freq[ singleTree ] += 1
            if len(freq) > maxType:
                if i - idxBgn > longestLen:
                    longestLen = i - idxBgn
                while True:
                    freq[ tree[idxBgn] ] -= 1
                    if freq[ tree[idxBgn] ] == 0:
                        del freq[ tree[idxBgn] ]
                    idxBgn += 1
                    if len(freq) <= maxType:
                        break

        if len(tree) - idxBgn > longestLen:
            longestLen = len(tree) - idxBgn

        return longestLen