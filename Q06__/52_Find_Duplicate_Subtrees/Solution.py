# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.treeFreq = {}
        self.travelBinaryTree(root)
        #print(self.treeFreq)
        outList = [ list(i) for i in self.treeFreq.keys() if self.treeFreq[i] > 1 ]

    def travelBinaryTree(self, root):
        if root.left != None and root.right != None:
            treeList = [ root.val ] + self.travelBinaryTree(root.left) + self.travelBinaryTree(root.right)
        elif root.left != None:
            treeList = [ root.val ] + self.travelBinaryTree(root.left)
        elif root.right != None:
            treeList = [ root.val ] + self.travelBinaryTree(root.right)
        else:
            treeList = [ root.val ]

        treeTuple = tuple(treeList)
        if treeTuple not in self.treeFreq:
            self.treeFreq[ treeTuple ] = 0
        self.treeFreq[ treeTuple ] += 1

        return treeList