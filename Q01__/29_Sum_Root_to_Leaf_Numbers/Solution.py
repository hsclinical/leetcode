# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return sum([ int(i) for i in self.travelTree(root) ])

    def travelTree(self, root):
        if root.left == None and root.right == None:
            return [ str(root.val) ]
        else:
            if root.right == None:
                numList = self.travelTree( root.left )
            elif root.left == None:
                numList = self.travelTree( root.right )
            else:
                lNumList = self.travelTree( root.left )
                rNumList = self.travelTree( root.right )
                numList = lNumList + rNumList
            outList = []
            for num in numList:
                newNum = str(root.val) + num
                outList.append( newNum )
            return outList
