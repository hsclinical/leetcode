from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        else:
            headNode, tailNode = self.headToTail(head)
            return headNode


    def headToTail(self, headNode):
        curNode = headNode
        while True:
            if curNode.child != None:
                childHead, childTail = self.headToTail(curNode.child)
                curNode.child = None
                nextNode = curNode.next
                curNode.next = childHead
                childHead.prev = curNode

                childTail.next = nextNode
                if nextNode == None:
                    tailNode = childTail
                else:
                    nextNode.prev = childTail
                    curNode = nextNode
            else:
                if curNode.next == None:
                    tailNode = curNode
                    break
                else:
                    curNode = curNode.next
        return headNode, tailNode
