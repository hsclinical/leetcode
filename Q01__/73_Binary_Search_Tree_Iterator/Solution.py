# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.valList = []
        self.travelTree( root )
        self.curIdx = -1
        self.valListLen = len(self.valList)

    def next(self) -> int:
        self.curIdx += 1
        return self.valList[ self.curIdx ]

    def hasNext(self) -> bool:
        if self.curIdx + 1 <= self.valListLen - 1:
            return True
        else:
            return False

    def travelTree(self, root):
        if root.left != None:
            self.travelTree(root.left)
        self.valList.append( root.val )
        if root.right != None:
            self.travelTree(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
