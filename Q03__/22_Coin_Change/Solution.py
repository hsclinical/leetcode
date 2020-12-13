from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # similar to the question that use combination of substring to build a whole string
        # use recursive
        if amount == 0:
            return 0
        else:
            coins.sort(reverse=True)
            minCoinNum = {}
            return self.coinCombination(coins, amount, minCoinNum)

    # input coins have been sorted from the largest to the smallest
    def coinCombination(self, coins, amount, minCoinNum):
        if amount in minCoinNum:
            return minCoinNum[amount]

        if amount < coins[-1]:
            minCoinNum[amount] = -1
            return -1
        elif amount in coins:
            minCoinNum[amount] = 1
            return 1
        else:
            found = False
            outAll = -1
            for coin in coins:
                if coin < amount:
                    outSingle = self.coinCombination(coins, amount-coin, minCoinNum)
                    if outSingle != -1:
                        if outAll == -1:
                            outAll = outSingle
                        else:
                            if outAll > outSingle:
                                outAll = outSingle
                        found = True
            if found:
                minCoinNum[amount] = outAll + 1
                return outAll + 1
            else:
                minCoinNum[amount] = -1
                return -1