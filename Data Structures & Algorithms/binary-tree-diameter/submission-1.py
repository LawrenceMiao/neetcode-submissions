# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# for each node, calculate proposed diameter = left heigh and right height
# calculate left height and right height
# height is max(left, right) + 1
class Solution:
    def __init__(self):
        self.maxDiameter = 0
    def calculateHeight(self, root):
        leftHeight = self.calculateHeight(root.left) if root.left else 0
        rightHeight = self.calculateHeight(root.right) if root.right else 0
        diameter = leftHeight + rightHeight
        self.maxDiameter = max(self.maxDiameter, diameter)

        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.calculateHeight(root)
        return self.maxDiameter
    
        