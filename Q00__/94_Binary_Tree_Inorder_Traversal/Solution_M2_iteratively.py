# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        else:
            curList = [ root ]
            while True:
                nextList = []
                expanded = False
                for curRoot in curList:
                    if curRoot.left != None:
                        nextList.append( curRoot.left )
                        expanded = True
                    curRootRight = curRoot.right
                    curRoot.left = None
                    curRoot.right = None
                    nextList.append( curRoot )
                    if curRootRight != None:
                        nextList.append( curRootRight )
                        expanded = True
                if expanded:
                    curList = nextList
                else:
                    break

            outList = [ x.val for x in curList ]
            return outList
