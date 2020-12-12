class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        else:
            info = []
            for i in range(len(start)):
                if start[i] == 'R' or start[i] == 'L':
                    info.append([i, start[i]])

            for i in range(len(end)):
                if end[i] == 'R' or end[i] == 'L':
                    if len(info) <= 0:
                        return False
                    checker = info.pop(0)
                    if checker[1] != end[i]:
                        return False
                    else:
                        if end[i] == 'R' and checker[0] <= i:
                            pass
                        elif end[i] == 'L' and checker[0] >= i:
                            pass
                        else:
                            return False
                        
            if len(info) == 0:
                return True
            else:
                return False
