# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if prev == None or prev.next == None: return head
        node = head.next
        head.next = None
        while node.next:
            nt = node.next
            #print(f"node:{node.val},node.next:{node.next.val}")
            node.next = prev
            #print(f"node:{node.val},node.next:{node.next.val}")
            #print("-")
            prev = node
            node = nt
        node.next = prev
        return node