# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build([0], preorder, inorder)

    def build(self, i: List[int], preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val = preorder[i[0]]
        node = TreeNode(val=val)
        if val not in inorder:
            return node

        idx = inorder.index(val)
        left = inorder[:idx]
        right = inorder[idx+1:]
        #print(val, preorder, inorder, left, right)
        if left:
            i[0]+=1
            node.left = self.build(i,preorder, left)
        if right:
            i[0]+=1
            node.right = self.build(i,preorder, right)
        return node