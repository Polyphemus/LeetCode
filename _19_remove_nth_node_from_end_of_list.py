# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# four attempt, after reading dicusssions. two pointers for a single pass, two loops, one to move leading pointer forward n
# another loop moves both until leading pointer reaches end 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        nodePointer = head
        trailPointer = head
        
        # move leading pointer forward n nodes
        for i in range(n):
            nodePointer = nodePointer.next
        
        # if pointer has reached None, n == sz and we want to pop first node
        if not nodePointer: 
            return head.next
        
        # move pointers along nodes until leading reach end. 
        while nodePointer.next:
            nodePointer = nodePointer.next
            trailPointer = trailPointer.next
            
        # Trailing set its .next to .next.next
        trailPointer.next = trailPointer.next.next
        return head    
        
