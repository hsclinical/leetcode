# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.rootList = []
        updatedRoot = self.delNodeBottomToTop(root, to_delete)
        if updatedRoot != None:
            self.rootList.append(updatedRoot)
        return self.rootList
    
    def delNodeBottomToTop(self, root, to_delete):
        if root.left != None:
            root.left = self.delNodeBottomToTop(root.left, to_delete)
        if root.right != None:
            root.right = self.delNodeBottomToTop(root.right, to_delete)

        if root.val in to_delete:
            if root.left != None:
                self.rootList.append(root.left)
            if root.right != None:
                self.rootList.append(root.right)
            return None
        else:
            return root
