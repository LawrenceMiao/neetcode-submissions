# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def findPath(root: TreeNode, child: TreeNode) -> tuple[list, bool]:
    # list is [left, right] from bottom to top

    if root is None:
        raise Exception("asdkjflkasj;lda")

    if root.val == child.val:
        return [], True

    if root.left is not None:
        leftPath, found = findPath(root.left, child)
        if found:
            leftPath.append("left")
            return leftPath, True
    
    if root.right is not None:
        rightPath, found = findPath(root.right, child)
        if found:
            rightPath.append("right")
            return rightPath, True
                
    return [], False


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # p_path, _ = findPath(root, p)
        # q_path, _ = findPath(root, q)
        # print(p_path, q_path)
        # curr_node = root
        # for i in range(len(p_path)):
        #     if i == len(q_path):
        #         break
        #     if p_path[-1 - i] == q_path[-1 - i]:
        #         curr_node = curr_node.left if p_path[-1-i] == "left" else curr_node.right
        #     else: # diverge
        #         break
        # return curr_node

        curr_node = root

        while curr_node:
            if curr_node.val < p.val and curr_node.val < q.val:
                curr_node = curr_node.right
            elif curr_node.val > p.val and curr_node.val > q.val:
                curr_node = curr_node.left
            else:
                return curr_node
            