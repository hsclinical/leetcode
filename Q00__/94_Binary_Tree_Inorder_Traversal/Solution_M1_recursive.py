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
            outList = []
            if root.left != None:
                outList += self.inorderTraversal( root.left )
            outList += [ root.val ]
            if root.right != None:
                outList += self.inorderTraversal( root.right )
            return outList
