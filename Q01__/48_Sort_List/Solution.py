# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        nodeList = []
        while True:
            if head == None:
                break
            else:
                nodeList.append( head )
                head = head.next
        nodeList = sorted( nodeList, key = lambda x: x.val )
        nodeList.append( None )
        for i in range( len(nodeList)-1 ):
            nodeList[i].next = nodeList[i+1]
        return nodeList[0]