# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def countGood(root: TreeNode, threshold: int) -> int:
    # recursive step v
    good = False
    if root.val >= threshold:
        threshold = root.val
        good = True

    # TODO: handle if root.left/right is null
    left_count = 0
    right_count = 0
    if root.left:
        left_count = countGood(root.left, threshold)
    if root.right:
        right_count = countGood(root.right, threshold)
    return left_count + right_count + (1 if good else 0)


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs recursive

        return countGood(root, root.val)