from typing import List
from datetime import datetime

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # v3.0.0:
        minDict = {}
        total = 0
        singleTotal = 0
        for j, num in enumerate(arr):
            if j != 0 and num >= arr[j-1]:
                # the current number is larger than or equal to the previous one
                # singleTotal keep the same, then plus "num"
                pass
            else:
                # the current number is smaller than the previous one
                for localMin in sorted(minDict.keys(), reverse=True):
                    if localMin <= num:
                        break
                    else:
                        singleTotal -= (localMin - num) * minDict[ localMin ]
                        if num in minDict:
                            minDict[ num ] += minDict[ localMin ]
                        else:
                            minDict[ num ] = minDict[ localMin ]
                        del minDict[ localMin ]

            if num in minDict:
                minDict[ num ] += 1
            else:
                minDict[ num ] = 1

            singleTotal += num
            total += singleTotal

        '''
        # v2.1.0: dict to merge localMin and update increasing case
        minDict = {}
        for j, num in enumerate(arr):
            if j != 0 and num > arr[j-1]:
                minDict[ num ] = 1
            else:
                singleTotal = 0
                for localMin in sorted(minDict.keys()):
                    if localMin <= num:
                        singleTotal += localMin * minDict[ localMin ]
                    else:
                        singleTotal += num * minDict[ localMin ]
                        if num in minDict:
                            minDict[ num ] += minDict[ localMin ]
                        else:
                            minDict[ num ] = minDict[ localMin ]
                        del minDict[ localMin ]

                if num in minDict:
                    minDict[ num ] += 1
                else:
                    minDict[ num ] = 1
            singleTotal += num
            total += singleTotal
            print(total, minDict)
            if j%10000 == 0:
                print("Now = " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        '''

        '''
        # v2.0.0: dict to merge localMin
        minDict = {}
        for j, num in enumerate(arr):
            for localMin in sorted(minDict.keys()):
                if localMin <= num:
                    total += localMin * minDict[ localMin ]
                else:
                    total += num * minDict[ localMin ]
                    if num in minDict:
                        minDict[ num ] += minDict[ localMin ]
                    else:
                        minDict[ num ] = minDict[ localMin ]
                    del minDict[ localMin ]

            if num in minDict:
                minDict[ num ] += 1
            else:
                minDict[ num ] = 1
            total += num
        '''

        '''
        # v1.1.0: enumerate for to process list
        # case #77: 41 sec
        minList = []
        for j, num in enumerate(arr):
            for i, localMin in enumerate(minList):
                if num < localMin:
                    minList[i] = num
                    total += num
                else:
                    total += localMin

            minList.append(num)
            total += num
            print(total)
        '''

        '''
        # v1.0.0: normal for to process list
        # case #77: 57 sec
        minList = []
        for num in arr:
            for i in range(len(minList)):
                if num < minList[i]:
                    minList[i] = num
                    total += num
                else:
                    total += minList[i]

            minList.append(num)
            total += num
        '''


        return total%(10**9 + 7)