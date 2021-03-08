# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        else:
            nodeList = []
            origHead = head
            while True:
                if head == None:
                    break
                else:
                    nodeList.append(head)
                    head = head.next

            for i in range(left, right):
                nodeList[i].next = nodeList[i-1]

            if left == 1:
                origHead = nodeList[right-1]
            else:
                nodeList[left-2].next = nodeList[right-1]

            if right == len(nodeList):
                nodeList[left-1].next = None
            else:
                nodeList[left-1].next = nodeList[right]

            return origHead
