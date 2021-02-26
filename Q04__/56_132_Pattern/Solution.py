class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        stackLow = []
        stackHigh = []
        outcome = False
        for i, num in enumerate(nums):
            if i == 0:
                stackLow.append(num)
            else:
                if num < stackLow[-1]:
                    if len(stackLow) == len(stackHigh):
                        stackLow.append(num)
                    else:
                        stackLow.pop()
                        stackLow.append(num)
                elif num > stackLow[-1]:
                    if len(stackLow) == len(stackHigh):
                        if num > stackHigh[-1]:
                            stackHigh.pop()
                            stackHigh.append(num)

                            stackLen = len(stackLow)
                            for i in range(stackLen-1, -1, -1):
                                if num <= stackLow[i]:
                                    break
                                else:
                                    if num < stackHigh[i]:
                                        outcome = True
                                        break
                                    else:
                                        pass
                        elif num < stackHigh[-1]:
                            outcome = True
                            break
                    else:
                        stackHigh.append(num)

                        stackLen = len(stackLow)
                        for i in range(stackLen-1, -1, -1):
                            if num <= stackLow[i]:
                                break
                            else:
                                if num < stackHigh[i]:
                                    outcome = True
                                    break
                                else:
                                    pass
        return outcome

