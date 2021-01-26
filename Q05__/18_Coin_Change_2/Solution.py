from typing import List
from functools import lru_cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        else:
            if len(coins) == 0:
                return 0

            coins = sorted(coins, reverse=True)
            if coins[-1] > amount:
                return 0
            else:
                return self.findCombination(tuple(coins), amount, 0, len(coins))

    @lru_cache(maxsize = None)
    def findCombination(self, coins, amount, initIdx, coinLen):
        cnt = 0
        for i in range(initIdx, coinLen):
            if coins[i] > amount:
                pass
            elif coins[i] == amount:
                cnt += 1
            else:
                cnt += self.findCombination(coins, amount-coins[i], i, coinLen)
        return cnt
