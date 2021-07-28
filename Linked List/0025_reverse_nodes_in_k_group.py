
# 25. Reverse Nodes in k-Group
#
# Source : https://leetcode.com/problems/reverse-nodes-in-k-group/
#
# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
#
# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the
# end, should remain as it is.
#
# You may not alter the values in the list's nodes, only nodes themselves may be changed.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head or k == 1:
            return head
        dummy = ListNode(-1)
        dummy.next = head

        # n is total number of nodes
        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        pre = dummy

        # n//k is number of reverse operations needed
        for l in range(n // k):
            cur = pre.next
            nxt = cur.next
            for i in range(k - 1):
                cur.next = nxt.next
                nxt.next = pre.next
                pre.next = nxt
                nxt = cur.next
            pre = cur
        return dummy.next


    #Referenced (for every K nodes perform reverse operation)
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        cur, cur_dummy = head, dummy
        length = 0

        while cur:
            next_cur = cur.next
            length = (length + 1) % k

            if length == 0:
                next_dummy = cur_dummy.next
                self.reverse(cur_dummy, cur.next)
                cur_dummy = next_dummy

            cur = next_cur

        return dummy.next


    def reverse(self, begin, end):
        first = begin.next
        cur = first.next

        while cur != end:
            first.next = cur.next
            cur.next = begin.next
            begin.next = cur
            cur = first.next


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]
