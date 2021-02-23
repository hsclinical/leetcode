class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slot1Len = len(slots1)
        slot2Len = len(slots2)
        sortedSlots1 = sorted(slots1)
        sortedSlots2 = sorted(slots2)
        curIdx1 = 0
        curIdx2 = 0
        overlaps = []
        while True:
            if sortedSlots1[curIdx1][1] < sortedSlots2[curIdx2][0]:
                curIdx1 += 1
            elif sortedSlots1[curIdx1][0] > sortedSlots2[curIdx2][1]:
                curIdx2 += 1
            elif sortedSlots1[curIdx1][0] <= sortedSlots2[curIdx2][0] and sortedSlots1[curIdx1][1] >= sortedSlots2[curIdx2][1]:
                overlaps.append( sortedSlots2[curIdx2] )
                curIdx2 += 1
            elif sortedSlots1[curIdx1][0] >= sortedSlots2[curIdx2][0] and sortedSlots1[curIdx1][1] <= sortedSlots2[curIdx2][1]:
                overlaps.append( sortedSlots1[curIdx1] )
                curIdx1 += 1
            elif sortedSlots1[curIdx1][0] <= sortedSlots2[curIdx2][1] and sortedSlots1[curIdx1][1] >= sortedSlots2[curIdx2][1]:
                overlaps.append( [ sortedSlots1[curIdx1][0], sortedSlots2[curIdx2][1] ] )
                curIdx2 += 1
            elif sortedSlots1[curIdx1][1] >= sortedSlots2[curIdx2][0] and sortedSlots1[curIdx1][1] <= sortedSlots2[curIdx2][1]:
                overlaps.append( [ sortedSlots2[curIdx2][0], sortedSlots1[curIdx1][1] ] )
                curIdx1 += 1
            else:
                print("Possible?")

            if curIdx1 >= slot1Len or curIdx2 >= slot2Len:
                break

        found = False
        for overlap in overlaps:
            if overlap[1] - overlap[0] >= duration:
                found = True
                return [ overlap[0], overlap[0]+duration ]

        if not found:
            return []
