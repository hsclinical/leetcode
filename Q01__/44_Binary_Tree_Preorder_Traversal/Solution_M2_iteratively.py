# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            curList = [ root ]
            while True:
                nextList = []
                expanded = False
                for curRoot in curList:
                    curRootLeft  = curRoot.left
                    curRootRight = curRoot.right
                    curRoot.left  = None
                    curRoot.right = None
                    nextList.append( curRoot )
                    if curRootLeft != None:
                        nextList.append( curRootLeft )
                        expanded = True
                    if curRootRight != None:
                        nextList.append( curRootRight )
                        expanded = True
                if expanded:
                    curList = nextList
                else:
                    break

            outList = [ x.val for x in curList ]
            return outList
