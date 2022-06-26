# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# 
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        ans = ListNode(None, head)
        l = ans
        r = l.next
        while r:
            m = l.next
            for h in range(k-1):
                try: 
                    r = r.next
                except AttributeError: 
                    return ans.next
            if not r:
                l.next = m
                return ans.next
            l.next = r
            l = m 
            r = r.next
            for i in range(k-1):
                for j in range(k - i - 2):
                    m = m.next
                m.next.next = m
                m = l
            l.next = r
        return ans.next
            
