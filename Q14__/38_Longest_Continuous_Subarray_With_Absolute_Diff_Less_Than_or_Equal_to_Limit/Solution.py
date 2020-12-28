import collections
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLen, i = 0, 0
        maxDeque, minDeque = collections.deque([]), collections.deque([])
        for j in range(len(nums)):
            while maxDeque and maxDeque[-1] < nums[j]:
                maxDeque.pop()
            maxDeque.append(nums[j])
            while minDeque and minDeque[-1] > nums[j]:
                minDeque.pop()
            minDeque.append(nums[j])

            if maxDeque[0] - minDeque[0] <= limit:
                maxLen = max(maxLen, j-i+1)
            else:
                if nums[i] == minDeque[0]:
                    minDeque.popleft()
                if nums[i] == maxDeque[0]:
                    maxDeque.popleft()
                i += 1
        return maxLen
