# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        # find root
        isNull = False
        while True:
            if root.val < low:
                if root.right == None:
                    # cannot find
                    isNull = True
                    break
                else:
                    root = root.right
            elif root.val > high:
                if root.left == None:
                    # cannot find
                    isNull = True
                    break
                else:
                    root = root.left
            else:
                break

        if isNull:
            return None

        if root.left != None:
            self.trimBSTWithMin(root, root.left, low)
        if root.right != None:
            self.trimBSTWithMax(root, root.right, high)

        return root


    def trimBSTWithMin(self, prevRoot, root, low):
        if root.val >= low:
            if root.left == None:
                pass
            else:
                self.trimBSTWithMin(root, root.left, low)
        else:
            if root.right == None:
                prevRoot.left = None
            else:
                prevRoot.left = root.right
                self.trimBSTWithMin(prevRoot, root.right, low)


    def trimBSTWithMax(self, prevRoot, root, high):
        if root.val <= high:
            if root.right == None:
                pass
            else:
                self.trimBSTWithMax(root, root.right, high)
        else:
            if root.left == None:
                prevRoot.right = None
            else:
                prevRoot.right = root.left
                self.trimBSTWithMax(prevRoot, root.left, high)

