
# 206. Reverse Linked List
#
# Source : https://leetcode.com/problems/reverse-linked-list/
#
# Given the head of a singly linked list, reverse the list, and return the reversed list.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        previous = None

        while head != None:
            temp = head.next
            head.next = previous
            previous = head
            head = temp

        return previous

    def reverseList1(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("-inf"))

        while head:
            dummy.next, head.next, head = head, dummy.next, head.next

            # or use this
            # temp = dummy.next
            # temp2 = head.next
            # dummy.next = head
            # head.next = temp
            # head = temp2

        return dummy.next


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]