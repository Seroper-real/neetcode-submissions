# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = None
        while list1 or list2:
            if list1 == None or (list2 != None and list1.val > list2.val):
                chosen = list2
                list2 = list2.next
            elif list2 == None or list1.val <= list2.val:
                chosen = list1
                list1 = list1.next
            
            if head == None:
                head = chosen
                node = head
            else:
                node.next = chosen
                node = node.next
        return head

