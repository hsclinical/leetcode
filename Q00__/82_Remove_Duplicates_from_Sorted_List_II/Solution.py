# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            nodeList = []
            lastNode = head
            isDuplicate = False
            head = head.next
            while True:
                if head == None:
                    if not isDuplicate:
                        nodeList.append(lastNode)
                    break
                if head.val == lastNode.val:
                    isDuplicate = True
                else:
                    if not isDuplicate:
                        nodeList.append(lastNode)
                    lastNode = head
                    isDuplicate = False
                head = head.next

            if len(nodeList) == 0:
                return None

            nodeLen = len(nodeList)
            for i in range(nodeLen):
                if i == nodeLen - 1:
                    nodeList[ i ].next = None
                else:
                    nodeList[ i ].next = nodeList[ i + 1 ]
            return nodeList[ 0 ]

