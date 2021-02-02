# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        found = False
        xNode = None
        curNodeList = [ root ]
        while True:
            nextNodeList = []
            for curNode in curNodeList:
                if curNode.val == x:
                    xNode = curNode
                    found = True
                    break
                else:
                    if curNode.left != None:
                        nextNodeList.append( curNode.left )
                    if curNode.right != None:
                        nextNodeList.append( curNode.right )
            if found:
                break
            else:
                curNodeList = nextNodeList

        if xNode.left == None:
            cntLeft = 0
        else:
            cntLeft = self.countNodeNum(xNode.left)

        if xNode.right == None:
            cntRight = 0
        else:
            cntRight = self.countNodeNum(xNode.right)

        cntParent = n - cntLeft - cntRight - 1

        if 2 * max(cntLeft, cntRight, cntParent) > n:
            return True
        else:
            return False


    def countNodeNum(self, root):
        if root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return 1 + self.countNodeNum( root.right )
        elif root.right == None:
            return 1 + self.countNodeNum( root.left )
        else:
            return 1 + self.countNodeNum( root.left ) + self.countNodeNum( root.right )
