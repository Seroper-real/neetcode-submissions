# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root, float('-inf'), float('+inf'))


    def traverse(self, node: Optional[TreeNode], lb: int, rb: int) -> bool:
        if node == None: return True
        if lb < node.val < rb:
            return self.traverse(node.left, lb, node.val) and self.traverse(node.right, node.val, rb)
        else: 
            return False
