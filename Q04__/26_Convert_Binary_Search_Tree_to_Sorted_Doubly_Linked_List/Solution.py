from typing import List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        else:
            headNode, tailNode = self.treeToList(root)
            headNode.left = tailNode
            tailNode.right = headNode
            return headNode

    def treeToList(self, root):
        if root == None:
            return None, None
        else:
            headNode = root
            tailNode = root
            if root.left != None:
                leftHeadNode,  leftTailNode  = self.treeToList(root.left)
                root.left = leftTailNode
                leftTailNode.right = root
                headNode = leftHeadNode
            if root.right != None:
                rightHeadNode, rightTailNode = self.treeToList(root.right)
                root.right = rightHeadNode
                rightHeadNode.left = root
                tailNode = rightTailNode
            return headNode, tailNode

