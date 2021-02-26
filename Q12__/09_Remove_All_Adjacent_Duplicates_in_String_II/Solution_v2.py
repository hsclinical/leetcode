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
                if len(set(stack[-(k-1):])) == 1:
                    stack = stack[:-(k-1)]
                else:
                    stack.append( char )
        return ''.join(stack)
