# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        store = deque()
        ret = []
        store.append(root)
        idx = 0
        while store:
            for _ in range(len(store)):
                node = store.popleft()
                if len(ret) <= idx:
                    ret.append(node.val)
                else: ret[idx] = node.val
                if node.left: store.append(node.left)
                if node.right: store.append(node.right)
            idx += 1
        return ret