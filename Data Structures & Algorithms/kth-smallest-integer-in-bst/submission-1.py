# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.traverse(root, arr)
        return arr[k-1]

    def traverse(self, node: Optional[TreeNode], arr: List[int]) -> None:
        if node == None: return
        if node.left: self.traverse(node.left, arr)
        arr.append(node.val)
        if node.right: self.traverse(node.right, arr)
        