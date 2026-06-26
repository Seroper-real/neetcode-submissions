# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 0
        node = head
        first_head = head
        start = head
        pre_start = None
        if k == 1: return head
        while node:
            i += 1
            #print(i,node.val)
            if i % k == 0:
                first_next = node.next
                hd, tl = self.reverse(start,k)
                if first_head == head: first_head = hd
                if pre_start != None:
                    pre_start.next = hd
                pre_start = tl
                start = first_next
                node = start
                tl.next = first_next
            else: node = node.next
        
        

        return first_head

    def reverse(self, head: Optional[ListNode], k: int) -> (Optional[ListNode], Optional[ListNode]):
        prev = None
        node = head
        i = 0
        while node and i < k:
            i += 1
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev, head #return head and tail of the reversed list
            

            