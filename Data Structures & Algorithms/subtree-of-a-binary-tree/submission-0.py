# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root, subRoot):
        if root == None and subRoot != None:
            return False
        if root != None and subRoot == None:
            return False
        if root == None and subRoot == None:
            return True
        if root.val == subRoot.val and self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right):
            return True
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot):
            return True
        if root.left and self.isSubtree(root.left, subRoot):
            return True
        if root.right and self.isSubtree(root.right, subRoot):
            return True
        return False
        