"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None: return None
        store = {}
        node = head
        new_head = None
        while node:
            new_node = self.get_node(store,node,node)
            new_node.random = self.get_node(store,node,node.random)
            new_node.next = self.get_node(store,node,node.next)
            if new_head == None: new_head = new_node
            node = node.next
        return new_head

    def get_node(self, store: Dict[Node, Node], node: 'Optional[Node]', child: 'Optional[Node]') -> 'Optional[Node]':
        if child:
            if child not in store:
                new_child = Node(child.val,None,None)
                store[child] = new_child
            else: new_child = store[child]
            return new_child
        return None

            
