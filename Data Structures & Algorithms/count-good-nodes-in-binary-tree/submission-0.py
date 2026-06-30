# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        self.traverse(root, root.val, count)
        return count[0]

    def traverse(self, node: Optional[TreeNode], mx: int, count: List[int]) -> None:
        if node:
            if node.val >= mx: count[0] += 1 #Found a good node
            mx = max(mx,node.val)
            if node.left: self.traverse(node.left, mx, count)
            if node.right: self.traverse(node.right, mx, count)