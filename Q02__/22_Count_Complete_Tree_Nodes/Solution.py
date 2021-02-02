# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        maxDepth = self.findLeftMaxDepth(root)
        if maxDepth <= 1:
            return maxDepth
        else:
            curRoot  = root
            curDepth = 1
            totalNum = 0
            while True:
                if curRoot.left == None:
                    totalNum += 1
                    break
                elif curRoot.right == None:
                    totalNum += 2
                    break
                elif self.findLeftMaxDepth(curRoot.right) + curDepth == maxDepth:
                    totalNum += 2 ** (maxDepth-curDepth)
                    curRoot = curRoot.right
                    curDepth += 1
                elif self.findRightMaxDepth(curRoot.left) + curDepth == maxDepth:
                    totalNum += 2 ** (maxDepth-curDepth-1)
                    totalNum += (2 ** (maxDepth-curDepth) - 1)
                    break
                else:
                    totalNum += 2 ** (maxDepth-curDepth-1)
                    curRoot = curRoot.left
                    curDepth += 1
            return totalNum


    def findLeftMaxDepth(self, root):
        if root == None:
            return 0
        elif root.left == None:
            return 1
        else:
            return 1 + self.findLeftMaxDepth(root.left)

    def findRightMaxDepth(self, root):
        if root == None:
            return 0
        elif root.right == None:
            return 1
        else:
            return 1 + self.findRightMaxDepth(root.right)