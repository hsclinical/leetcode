# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        return self.constructFBT(n)

    def constructFBT(self, n):
        if n % 2 == 0:
            return []
        elif n == 1:
            nodeRoot  = TreeNode(0)
            return [ nodeRoot ]
        elif n == 3:
            nodeLeft  = TreeNode(0)
            nodeRight = TreeNode(0)
            nodeRoot  = TreeNode(0, nodeLeft, nodeRight)
            return [ nodeRoot ]
        else:
            outList = []
            for i in range(1, n, 2):
                nLeft = i
                nRight = n - 1 - nLeft
                listLeft = self.constructFBT(nLeft)
                listRight = self.constructFBT(nRight)
                for nodeLeft in listLeft:
                    for nodeRight in listRight:
                        nodeRoot  = TreeNode(0, nodeLeft, nodeRight)
                        outList.append(nodeRoot)
            return outList


