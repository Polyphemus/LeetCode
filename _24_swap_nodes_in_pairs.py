# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if head.next == None:
            return head
        
        ans = ListNode(None, head)
        l = ans
        m = head
        r = head.next

        #
        while m.next and r.next:
            l.next = r
            m.next = r.next
            r.next = m
            l = m
            m = m.next
            r = m.next
            
        if m.next:
            l.next = r
            m.next = r.next
            r.next = m
        
        return ans.next
