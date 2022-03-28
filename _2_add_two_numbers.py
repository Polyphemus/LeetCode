# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        total = 0

        current = l1
        i = 0
        while current != None:
            total = total + current.val * pow(10, i)
            current = current.next
            i += 1

        current = l2
        i = 0
        while current != None:
            total = total + current.val * pow(10, i)
            current = current.next
            i += 1

        totalStr = str(int(total))
        a1 = ListNode(int(totalStr[len(totalStr) - 1]))
        current = a1

        for i in range(len(totalStr) - 2, -1, -1):
            current.next = ListNode(totalStr[i])
            current = current.next

        return a1
