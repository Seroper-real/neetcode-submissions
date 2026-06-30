# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        store = deque()
        ret = []
        store.append((0,root))
        while store:
            depth, node = store.popleft()
            if len(ret) <= depth:
                ret.append([node.val])
            else: ret[depth].append(node.val)
            if node.left: store.append((depth+1, node.left))
            if node.right: store.append((depth+1, node.right))
        return ret