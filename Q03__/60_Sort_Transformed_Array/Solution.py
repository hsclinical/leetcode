class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        numLen = len(nums)
        medNums = [ a * num * num + b * num + c for num in nums ]
        if a > 0:
            idxMin = medNums.index( min(medNums) )
            if idxMin == 0:
                return medNums
            elif idxMin == numLen - 1:
                return reversed(medNums)
            else:
                outNums = [ medNums[idxMin] ]
                idxLeft = idxMin - 1
                idxRight = idxMin + 1
                while True:
                    if idxLeft < 0 and idxRight >= numLen:
                        break
                    elif idxLeft < 0:
                        outNums.append( medNums[idxRight] )
                        idxRight += 1
                    elif idxRight >= numLen:
                        outNums.append( medNums[idxLeft] )
                        idxLeft -= 1
                    else:
                        if medNums[idxRight] <= medNums[idxLeft]:
                            outNums.append( medNums[idxRight] )
                            idxRight += 1
                        else:
                            outNums.append( medNums[idxLeft] )
                            idxLeft -= 1
                return outNums
        elif a <= 0:
            idxMax = medNums.index( max(medNums) )
            if idxMax == 0:
                return reversed(medNums)
            elif idxMax == numLen - 1:
                return medNums
            else:
                outNums = [ medNums[idxMax] ]
                idxLeft = idxMax - 1
                idxRight = idxMax + 1
                while True:
                    if idxLeft < 0 and idxRight >= numLen:
                        break
                    elif idxLeft < 0:
                        outNums.append( medNums[idxRight] )
                        idxRight += 1
                    elif idxRight >= numLen:
                        outNums.append( medNums[idxLeft] )
                        idxLeft -= 1
                    else:
                        if medNums[idxRight] > medNums[idxLeft]:
                            outNums.append( medNums[idxRight] )
                            idxRight += 1
                        else:
                            outNums.append( medNums[idxLeft] )
                            idxLeft -= 1
                return reversed(outNums)
        else:
            # a == 0
            if b >= 0:
                return medNums
            else:
                return reversed(medNums)