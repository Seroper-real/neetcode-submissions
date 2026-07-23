# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None: return str(None)
        store = deque()
        store.append(root)
        serialized = ""
        node = root
        while store:
            node = store.popleft()
            val = None
            if node:
                val = node.val
                store.append(node.left)
                store.append(node.right)

            serialized += str(val)+"-"
        #print(serialized[:-1])
        return serialized[:-1]


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split("-")
        
        if self._int(arr[0]) == None: return None

        val_store = deque()
        node_store = deque()
        for val in arr: val_store.append(val)
        
        val = self._int(val_store.popleft())
        root = TreeNode(val)
        node_store.append(root)
        while val_store:
            node = node_store.popleft()
            val_l = self._int(val_store.popleft())
            if val_l != None:
                node_left = TreeNode(val_l)
                node.left = node_left
                node_store.append(node_left)
            
            val_r = self._int(val_store.popleft())
            if val_r != None:
                node_right = TreeNode(val_r)
                node.right = node_right
                node_store.append(node_right)

        return root

    def _int(self, data: str) -> Optional[int]:
        if data == 'None': return None
        return int(data)







