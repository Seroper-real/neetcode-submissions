# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
       mx = [0]
       self.traverse(root, mx)
       return mx[0]

    def traverse(self, node: Optional[TreeNode], mx: List[int]) -> int:
        if node == None or (node.left == None and node.right == None): return 0
        path_l, path_r = 0, 0
        if node.left: path_l = 1 + self.traverse(node.left, mx)
        if node.right: path_r = 1 + self.traverse(node.right, mx)
        mx[0] = max(mx[0], path_l + path_r)
        return max(path_l, path_r)
