# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None

        # build empty node, num -> node
        numToNodeDict = dict([ (num, TreeNode(num)) for num in preorder])

        root = numToNodeDict[ preorder[0] ]
        confirmed = set()
        while True:
            remainLen = len(preorder)
            if remainLen == 1:
                break
            else:
                curIdx = 0
                while True:
                    if curIdx + 1 < len(preorder):
                        curNum  = preorder[ curIdx ]
                        nextNum = preorder[ curIdx+1 ]
                        curIdxFromIn  = inorder.index( curNum )
                        nextIdxFromIn = inorder.index( nextNum )

                        if curIdxFromIn - nextIdxFromIn == 1:
                            tmpNode = numToNodeDict[ curNum ]
                            while True:
                                if tmpNode.left == None:
                                    tmpNode.left = numToNodeDict[ nextNum ]
                                    break
                                else:
                                    tmpNode = tmpNode.left
                            #numToNodeDict[ curNum ].left = numToNodeDict[ nextNum ]
                            confirmed.add( nextNum )
                            del preorder[ curIdx+1 ]
                            del inorder[ nextIdxFromIn ]
                        elif curIdxFromIn - nextIdxFromIn == -1:
                            tmpNode = numToNodeDict[ curNum ]
                            while True:
                                if tmpNode.right == None:
                                    tmpNode.right = numToNodeDict[ nextNum ]
                                    break
                                else:
                                    tmpNode = tmpNode.right
                            #numToNodeDict[ curNum ].right = numToNodeDict[ nextNum ]
                            confirmed.add( nextNum )
                            del preorder[ curIdx+1 ]
                            del inorder[ nextIdxFromIn ]
                        else:
                            curIdx += 1
                    else:
                        break

        return root
