# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if root == None:
            return 0

        (tile, numSum) = self.findTiltSupl( root )
        return tile


    def findTiltSupl(self, root: TreeNode):
        if root == None:
            return (0, 0)
        elif root.left == None and root.right == None:
            return (0, root.val)
        elif root.left == None:
            (tile, numSum) = self.findTiltSupl( root.right )
            return (abs( numSum ) + tile, numSum + root.val)
        elif root.right == None:
            (tile, numSum) = self.findTiltSupl( root.left )
            return (abs( numSum ) + tile, numSum + root.val)
        else:
            (tileRight, numSumRight) = self.findTiltSupl( root.right )
            (tileLeft,  numSumLeft)  = self.findTiltSupl( root.left )

            return (abs( numSumLeft - numSumRight ) + tileLeft + tileRight, root.val + numSumLeft + numSumRight)
