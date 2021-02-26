from typing import List

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s

        stack = []
        for char in s:
            if len(stack) < k - 1 or stack[-1] != char:
                stack.append( char )
            else:
                toRemove = True
                for i in range(1, k):
                    if stack[ -i ] != char:
                        toRemove = False
                        break
                if toRemove:
                    for i in range(1, k):
                        stack.pop()
                else:
                    stack.append( char )
        return ''.join(stack)
