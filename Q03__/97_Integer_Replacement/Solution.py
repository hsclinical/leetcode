from typing import List
from functools import lru_cache

class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.searchPath(n)

    @lru_cache(maxsize=None)
    def searchPath(self, n):
        if n == 1:
            return 0
        else:
            if n % 2 == 0:
                return 1 + self.searchPath( n/2 )
            else:
                return 1 + min( self.searchPath( n+1 ), self.searchPath( n-1 ))
