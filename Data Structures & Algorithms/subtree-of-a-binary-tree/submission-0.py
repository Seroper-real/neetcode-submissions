# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.sameTree(root, subRoot): return True
        if root == None: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if a == None and b == None: return True
        if a == None or b == None or a.val != b.val: return False
        return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)