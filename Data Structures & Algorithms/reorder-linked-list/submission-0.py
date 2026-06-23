# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = 0
        node = head
        while node != None:
            l += 1
            node = node.next
        
        n = (l+1) // 2

        #Reverse first n element of ll
        prev, node = None, head
        for _ in range(n):
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        
        l1 = prev #l1 has first n elements in reverse order
        l2 = node #l2 has last l-n elements in regular order
        
        #self.print_ll(l1)
        #self.print_ll(l2)

        #Compose the result mixing l1 and l2
        #If starting list has even or odd elements, changes the order for mixing elements up
        if l % 2 == 0:
            n2, n1 = l1, l2
        else:
            n1, n2 = l1, l2
        rev_head = n1
        while n1 and n2:                
            tmp1 = n1.next
            tmp2 = n2.next
            n1.next = n2
            n2.next = tmp1
            n1 = tmp1
            n2 = tmp2

        #self.print_ll(rev_head)
        #Reversing the order of the result
        prev, node = None, rev_head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        head = prev

    def print_ll(self, ll: Optional[ListNode]) -> None:
        #Not needed for the solution, just utils for debugging
        node = ll
        s = ""
        while node != None:
            s += f"{node.val}->"
            node = node.next
        print(s[:len(s)-2])