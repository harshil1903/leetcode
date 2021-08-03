
# 19. Remove Nth Node From End of List
#
# Source : https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#
# Given the head of a linked list, remove the nth node from the end of the list and return its head.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        # move to nth node
        for i in range(n):
            fast = fast.next

        # moving fast to end of list will bring slow to nth node from the end of list
        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]