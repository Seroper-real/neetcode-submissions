# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        store = {}
        self.traverse(root, store)
        print(store)
        mx = [float('-inf')]
        self.find_max(root, store, mx)
        return mx[0]

    def traverse(self, node: Optional[TreeNode], store: Dict(int, int)) -> int:
        if node.left == None and node.right == None:
            store[node] = node.val
            return node.val
        
        left_best = float('-inf')
        right_best = float('-inf')
        
        if node.left: left_best = self.traverse(node.left, store)
        if node.right: right_best = self.traverse(node.right, store)

        mx = max(left_best + node.val, right_best + node.val, node.val)
        store[node] = mx
        return mx

    def find_max(self, node: Optional[TreeNode], store: Dict(int, int), mx: List[int]) -> None:
        max_left = store[node.left] if node.left else 0
        max_right = store[node.right] if node.right else 0
        node_max = max(node.val, node.val+max_left, node.val+max_right, node.val+max_right+max_left)
        mx[0] = max(mx[0], node_max)
        if node.left: self.find_max(node.left, store, mx)
        if node.right: self.find_max(node.right, store, mx)