# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [ target.val ]
        else:
            self.nodeDict = {}
            self.nodeDict[ target ] = 0
            self.scanTree( root, target, K )

            self.nodeList = []
            for curNode in self.nodeDict:
                self.scanTopDown( curNode, K - self.nodeDict[ curNode ], target )
            return self.nodeList


    def scanTree(self, root, target, K):
        if root.val == target.val:
            return True, 0
        else:
            if root.left != None:
                lFound, lRelDist = self.scanTree(root.left, target, K)
            else:
                lFound = False
                lRelDist = 0

            if root.right != None:
                rFound, rRelDist = self.scanTree(root.right, target, K)
            else:
                rFound = False
                rRelDist = 0

            if lFound and lRelDist + 1 <= K:
                self.nodeDict[ root ] = lRelDist + 1
                return True, lRelDist + 1
            elif rFound and rRelDist + 1 <= K:
                self.nodeDict[ root ] = rRelDist + 1
                return True, rRelDist + 1
            else:
                return False, 0


    def scanTopDown(self, root, K, target):
        if K == 0:
            self.nodeList.append( root.val )
        else:
            if root.left != None and root.left not in self.nodeDict:
                self.scanTopDown(root.left, K-1, target)
            if root.right != None and root.right not in self.nodeDict:
                self.scanTopDown(root.right, K-1, target)
