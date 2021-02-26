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
            outList = []
            outList += [ root.val ]
            if root.left != None:
                outList += self.preorderTraversal( root.left )
            if root.right != None:
                outList += self.preorderTraversal( root.right )
            return outList
