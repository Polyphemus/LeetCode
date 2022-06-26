# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# 
# Merge all the linked-lists into one sorted linked-list and return it.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists):
            return None
        
        regLists = []
        for i in range(len(lists)):
            pointer = lists[i]
            while pointer: 
                regLists.append(pointer.val)
                pointer = pointer.next
        
        regLists.sort()
        ans = ListNode(regLists[0], None)
        pointer2 = ans
        for i in range(len(regLists) - 1):
            pointer2.next = ListNode(regLists[i+1])
            pointer2 = pointer2.next   
        
        return ans
