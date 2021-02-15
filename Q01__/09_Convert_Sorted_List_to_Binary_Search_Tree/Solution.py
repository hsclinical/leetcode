# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if head == None:
            return head
        elif head.next == None:
            return TreeNode(head.val)
        else:
            nodeList = []
            while True:
                if head == None:
                    break
                else:
                    nodeList.append( TreeNode(head.val) )
                    head = head.next
            return self.buildTree(nodeList, 0, len(nodeList)-1)

    def buildTree(self, nodeList, bgnIdx, endIdx):
        if endIdx - bgnIdx == 0:
            return nodeList[ endIdx ]
        elif endIdx - bgnIdx == 1:
            nodeList[ endIdx ].left = nodeList[ bgnIdx ]
            return nodeList[ endIdx ]
        else:
            midIdx = (bgnIdx + endIdx) // 2
            nodeList[ midIdx ].left  = self.buildTree(nodeList, bgnIdx, midIdx-1)
            nodeList[ midIdx ].right = self.buildTree(nodeList, midIdx+1, endIdx)
            return nodeList[ midIdx ]
