from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        handLength = len(hand)
        if handLength%W != 0:
            return False
        else:
            cardCount = {}
            for card in hand:
                if card in cardCount:
                    cardCount[ card ] += 1
                else:
                    cardCount[ card ] = 1

            output = True
            sortedKeys = sorted(cardCount.keys())
            for i in range(len(sortedKeys)):
                initCount = cardCount[ sortedKeys[i] ]
                if initCount != 0:
                    for j in range(W):
                        if sortedKeys[i] + j in cardCount and cardCount[ sortedKeys[i] + j ] >= initCount:
                            cardCount[ sortedKeys[i] + j ] -= initCount
                        else:
                            output = False
                            break
                    if not output:
                        break
            return output
