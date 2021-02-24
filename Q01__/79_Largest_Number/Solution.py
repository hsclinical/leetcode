from typing import List
import functools, re

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strNums = [ str(num) for num in nums ]

        def compare(item1, item2):
            case1 = item1 + item2
            case2 = item2 + item1
            if case1 < case2:
                return 1
            elif case1 > case2:
                return -1
            else:
                return 0

        strNums.sort( key=functools.cmp_to_key(compare) )
        if strNums[0] == '0':
            return '0'
        else:
            return ''.join(strNums)

