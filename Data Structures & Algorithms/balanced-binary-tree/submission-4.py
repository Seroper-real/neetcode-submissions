# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        balancedL, deepL = self.traverse(root.left)
        if not balancedL: return False
        balancedR, deepR = self.traverse(root.right)
        return balancedR and max(deepL,deepR) <= min(deepL,deepR)+1
        
    def traverse(self, root: Optional[TreeNode]) -> (bool, int):
        isBalanced = True
        if root == None:
            return True, 0
        elif (root.left and root.right) or (root.left == None and root.right == None) or (root.left and root.left.left == None and root.left.right == None) or (root.right and root.right.left == None and root.right.right == None):
            #is balanced, keep going
            deepL, deepR, = 1, 1
            if root.left:
                isBalanced, dl = self.traverse(root.left)
                deepL += dl
            if isBalanced and root.right:
                isBalanced, dr = self.traverse(root.right)
                deepR += dr
            return isBalanced, max(deepL,deepR)
        else:
            return False, 0
