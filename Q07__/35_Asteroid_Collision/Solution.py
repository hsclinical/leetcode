class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stackNum = []
        for i, asteroid in enumerate(asteroids):
            while True:
                if len(stackNum) == 0:
                    stackNum.append( asteroid )
                    break
                else:
                    if stackNum[-1] * asteroid > 0:
                        stackNum.append( asteroid )
                        break
                    elif stackNum[-1] < 0 and asteroid > 0:
                        stackNum.append( asteroid )
                        break
                    else:
                        if abs(stackNum[-1]) == abs(asteroid):
                            stackNum.pop()
                            break
                        elif abs(stackNum[-1]) > abs(asteroid):
                            break
                        else:
                            stackNum.pop()
        return stackNum

