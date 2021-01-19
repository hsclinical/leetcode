from typing import List
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.priceTuple = tuple(price)
        self.specialTuple = tuple(map(tuple, special))
        skipSet = set()
        self.needsLen = len(needs)
        return self.addOffer(tuple(skipSet), tuple(needs))

    @lru_cache(maxsize=None)
    def addOffer(self, skipSet, needs):
        totalPrice = 0
        for i, singlePrice in enumerate(self.priceTuple):
            totalPrice += singlePrice * needs[i]

        nextSkipSet = set([i for i in skipSet])
        for i, offer in enumerate(self.specialTuple):
            if i not in skipSet:
                validOffer = True
                nextNeeds = [0] * self.needsLen
                for j, singleNeed in enumerate(needs):
                    if singleNeed < offer[j]:
                        validOffer = False
                        break
                    else:
                        nextNeeds[j] = singleNeed - offer[j]
                if validOffer:
                    candTotalPrice = offer[-1] + self.addOffer(tuple(nextSkipSet), tuple(nextNeeds))
                    if candTotalPrice < totalPrice:
                        totalPrice = candTotalPrice
                else:
                    nextSkipSet.add(i)

        return totalPrice

