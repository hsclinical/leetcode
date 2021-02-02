# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 == None and root2 == None:
            return True
        elif root1 != None and root2 != None:
            return self.compareCurrentNode(root1, root2)
        else:
            return False

    def compareCurrentNode(self, root1, root2):
        if root1.val != root2.val:
            return False
        else:
            outcome = False
            if self.equalNode(root1.left, root2.left) and self.equalNode(root1.right, root2.right):
                outcome = True
            elif self.equalNode(root1.left, root2.right) and self.equalNode(root1.right, root2.left):
                # flip
                tmp = root2.right
                root2.right = root2.left
                root2.left = tmp
                outcome = True

            if outcome:
                if root1.left != None:
                    lChild = self.compareCurrentNode(root1.left, root2.left)
                else:
                    lChild = True

                if root1.right != None:
                    rChild = self.compareCurrentNode(root1.right, root2.right)
                else:
                    rChild = True

                if lChild and rChild:
                    return True
                else:
                    return False
            else:
                return False

    def equalNode(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        elif root1 != None and root2 != None and root1.val == root2.val:
            return True
        else:
            return False