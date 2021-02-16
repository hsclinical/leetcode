from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        freq = defaultdict(int)
        for num in nums:
            freq[ num ] += 1
        keys = [ num for num, val in sorted(freq.items(), key=lambda item: item[1], reverse=True) ]
        return keys[:k]