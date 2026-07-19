# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx = [float('-inf')]
        self.traverse(root, mx)
        return mx[0]

    def traverse(self, node: Optional[TreeNode], mx: List[int]) -> int:
        if not node: return 0
        
        left = self.traverse(node.left, mx)
        right = self.traverse(node.right, mx)

        mx[0] = max(mx[0], node.val + max(left,0) + max(right,0))
 
        return node.val + max(left, right, 0)