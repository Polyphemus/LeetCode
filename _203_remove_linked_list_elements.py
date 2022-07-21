# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:     
        if head == None:
            return(head)
        if head.next == None:
            if head.val == val:
                return(None)
            else:
                return(head)
                
        pointer = head
        # iterate through until pointer is at node with value other than val
        while pointer.val == val:
            if pointer.next == None:
                return(None)
            else:
                pointer = pointer.next
        head = pointer # set head to first node with non val value
        
        while pointer.next != None:
            print(pointer.val)
            if pointer.next.val == val and pointer.next.next == None : # if next value is val and the last node, set current next to None
                pointer.next = None
                return(head)
            elif pointer.next.val == val:
                pointer.next = pointer.next.next 
            if pointer.next.val != val: ## move to next node only if next value isn't val
                pointer = pointer.next
        return(head)
        
