# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:    
        if root == None: return True
        if not self.isBalancedNode(root): return False
        isbalanced = True
        if root.left: isbalanced = self.isBalanced(root.left)
        if isbalanced and root.right: isbalanced = self.isBalanced(root.right)
        return isbalanced
        
    
    def isBalancedNode(self, root: Optional[TreeNode]) -> bool:
        if root:
            depth_l, depth_r = 0, 0
            if root.left: depth_l = 1 + self.traverse(root.left)
            if root.right: depth_r = 1 + self.traverse(root.right)
            if max(depth_l, depth_r) > min(depth_l, depth_r) + 1: return False
        return True

    def traverse(self, root: Optional[TreeNode]) -> int:
        if root == None: return 0

        depth_l, depth_r = 0, 0
        if root.left: depth_l = 1 + self.traverse(root.left)
        if root.right: depth_r = 1 + self.traverse(root.right)

        return max(depth_l, depth_r)
