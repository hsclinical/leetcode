# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        outList = []
        curList = []
        while True:
            if head == None:
                break

            if head.val in G:
                curList.append( head.val )
            else:
                if len(curList) != 0:
                    outList.append( curList )
                    curList = []
            head = head.next

        if len(curList) != 0:
            outList.append( curList )
        return len(outList)
