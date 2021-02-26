from typing import List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head == None:
            return []

        stackIdx = []
        stackVal = []
        idxToNum = {}
        cnt = 0
        while True:
            if head == None:
                break
            else:
                while True:
                    if len(stackVal) > 0 and head.val > stackVal[-1]:
                        preNum = stackVal.pop()
                        preIdx = stackIdx.pop()
                        idxToNum[ preIdx ] = head.val
                    else:
                        stackVal.append(head.val)
                        stackIdx.append(cnt)
                        break
                cnt += 1
                head = head.next

        if len(stackIdx) != 0:
            for idx in stackIdx:
                idxToNum[ idx ] = 0

        outList = [ idxToNum[idx] for idx in sorted(idxToNum.keys()) ]
        return outList