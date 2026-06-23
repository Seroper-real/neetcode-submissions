# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False
        store = set()
        node = head
        while node.next not in store:
            if node.next == None: return False
            store.add(node.next)
            node = node.next
        return True