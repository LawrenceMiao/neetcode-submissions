# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])
        out = []
        if root is None:
            return []

        while q:
            level_count = len(q)

            right_node = 0
            for i in range(level_count):
                right_node = q.popleft()
                if right_node.left:
                    q.append(right_node.left)
                if right_node.right:
                    q.append(right_node.right)

            out.append(right_node.val)



        return out
