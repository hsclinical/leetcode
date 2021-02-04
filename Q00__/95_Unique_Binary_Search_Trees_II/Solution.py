# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.subtree(n, 0)

    def subtree(self, n, valOffset):
        if n == 1:
            root = TreeNode( n + valOffset, None, None )
            return [ root ]
        else:
            rootList = []
            for i in range(1, n+1):
                nLeft = i - 1
                nRight = n - i
                if nLeft == 0:
                    rightList = self.subtree(nRight, i + valOffset)
                    for rightNode in rightList:
                        root = TreeNode( i + valOffset, None, rightNode )
                        rootList.append( root )
                elif nRight == 0:
                    leftList = self.subtree(nLeft, valOffset)
                    for leftNode in leftList:
                        root = TreeNode( i + valOffset, leftNode, None )
                        rootList.append( root )
                else:
                    leftList = self.subtree(nLeft, valOffset)
                    rightList = self.subtree(nRight, i + valOffset)
                    for leftNode in leftList:
                        for rightNode in rightList:
                            root = TreeNode( i + valOffset, leftNode, rightNode )
                            rootList.append( root )
            return rootList

