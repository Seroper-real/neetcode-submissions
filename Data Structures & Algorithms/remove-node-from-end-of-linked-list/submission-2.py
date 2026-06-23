# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        node = head
        while node:
            l+=1
            node = node.next
        i = 0
        if i == l-n: return head.next
        tmp, node = head, head
        while node:
            if i == l-n:
                tmp.next = node.next
                break
            i+=1
            tmp = node
            node = node.next
        return head