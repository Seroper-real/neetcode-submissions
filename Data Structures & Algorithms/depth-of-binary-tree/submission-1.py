# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return self.traverse(root, 0)

    def traverse(self, node: Optional[TreeNode], depth: int) -> int:
        depth += 1
        depth_l = 0
        depth_r = 0
        if node.left: depth_l = self.traverse(node.left, depth)
        if node.right: depth_r = self.traverse(node.right, depth)
        return max(depth, depth_l, depth_r)