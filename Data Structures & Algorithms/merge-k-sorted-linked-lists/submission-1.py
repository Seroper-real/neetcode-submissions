# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while True:
            mn = float('inf')
            chosen = -1
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val <= mn:
                        chosen = i
                        mn = lists[i].val
            if chosen == -1: return dummy.next #No values left, is sorted!
            
            node.next = lists[chosen]
            lists[chosen] = lists[chosen].next
            node = node.next
            node.next = None #unlink node with rest of the list