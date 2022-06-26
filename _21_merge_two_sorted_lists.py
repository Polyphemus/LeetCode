# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.q

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # in the diagram the lists are parallel so pointer will be top and bottom
        t = list1
        b = list2
        
        ansHead = ListNode(None, None)        
        ans = ansHead
        
        # loops until one pointer reaches tail node
        while t and b:
            if t.val < b.val:
                ans.next = t
                t = t.next              
                ans = ans.next
                
            elif b.val < t.val:
                ans.next = b
                b = b.next
                ans = ans.next
                
            else:
                ans.next = ListNode(t.val, b)
                b = b.next
                t = t.next
                ans = ans.next.next

        if t:
            ans.next = t           
        else:
            ans.next = b
        return ansHead.next
