# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        matrix = [ [ [ ] for _ in range(199) ] for _ in range(100) ]
        curX = 99
        curY = 0
        self.minX = 99
        self.maxX = 99
        self.maxY = 0
        self.scanTree(matrix, root, curY, curX)

        outList = []
        for x in range(self.minX, (self.maxX+1)):
            single = []
            for y in range(self.maxY+1):
                single += matrix[y][x]
            outList.append( single )
        return outList

    def scanTree(self, matrix, curNode, y, x):
        matrix[y][x].append(curNode.val)
        if y > self.maxY:
            self.maxY = y
        if x > self.maxX:
            self.maxX = x
        if x < self.minX:
            self.minX = x
        if curNode.left != None:
            self.scanTree(matrix, curNode.left, y+1, x-1)
        if curNode.right != None:
            self.scanTree(matrix, curNode.right, y+1, x+1)
