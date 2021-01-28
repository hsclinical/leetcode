# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            val1, val2 = self.maxAmount(root)
            return max(val1, val2)

    def maxAmount(self, root):
        # return two values: 1. values with this node; 2. values without this node
        if root.left == None and root.right == None:
            return(root.val, 0)
        elif root.left == None:
            rightVal1, rightVal2 = self.maxAmount(root.right)
            return(max(rightVal2 + root.val, rightVal1), max(rightVal1, rightVal2))
        elif root.right == None:
            leftVal1, leftVal2 = self.maxAmount(root.left)
            return(max(leftVal2 + root.val, leftVal1), max(leftVal1, leftVal2))
        else:
            leftVal1,  leftVal2  = self.maxAmount(root.left)
            rightVal1, rightVal2 = self.maxAmount(root.right)

            rootVal1 = max(leftVal2 + rightVal2 + root.val, leftVal1 + rightVal1)
            rootVal2 = max(leftVal1 + rightVal1, leftVal1 + rightVal2, leftVal2 + rightVal1)
            return(rootVal1, rootVal2)
