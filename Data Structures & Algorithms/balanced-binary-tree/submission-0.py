# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.b = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        self.height(root)
        return self.b
    def height(self, root):
        leftHeight = 1+ self.height(root.left) if root.left else 0
        rightHeight = 1+self.height(root.right) if root.right else 0
        if abs(leftHeight - rightHeight) > 1:
            self.b = False
        return max(leftHeight, rightHeight)