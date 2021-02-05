from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushLen = len(pushed)
        popLen = len(popped)
        if pushLen != popLen:
            return False
        else:
            if len(pushed) == 0:
                return True
            else:
                curStack = []
                curStack.append(pushed[0])
                pushIdx = 1
                popIdx = 0
                return self.actionToPushNPop(curStack, pushed, pushLen, pushIdx, popped, popLen, popIdx)


    def actionToPushNPop(self, curStack, pushed, pushLen, pushIdx, popped, popLen, popIdx):
        if pushIdx == pushLen:
            if popIdx == popLen and len(curStack) == 0:
                return True
            else:
                if popped[popIdx] == curStack[-1]:
                    curStack.pop()
                    return self.actionToPushNPop(curStack, pushed, pushLen, pushIdx, popped, popLen, popIdx+1)
                else:
                    return False
        else:
            if len(curStack) > 0 and popped[popIdx] == curStack[-1]:
                # two choices: push or pop
                newStack = curStack[:]
                curStack.append(pushed[ pushIdx ])
                pushOutcome = self.actionToPushNPop(curStack, pushed, pushLen, pushIdx+1, popped, popLen, popIdx)

                newStack.pop()
                popOutcome = self.actionToPushNPop(newStack, pushed, pushLen, pushIdx, popped, popLen, popIdx+1)

                if pushOutcome or popOutcome:
                    return True
                else:
                    return False
            else:
                # one choice only: push
                curStack.append(pushed[ pushIdx ])
                return self.actionToPushNPop(curStack, pushed, pushLen, pushIdx+1, popped, popLen, popIdx)
