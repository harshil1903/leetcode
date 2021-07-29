
# 23. Merge k Sorted Lists
#
# Source : https://leetcode.com/problems/merge-k-sorted-lists/
#
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.



# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        # merge two lists at a time
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        left, right = 0, len(lists) - 1

        # loop till all lists are merged and stored in first half of lists
        # for eg. Lists   :  1 2 3 4 5
        #         1st loop:  1(1,5)     2(2,4)    3    at 3, left==right so reset left, loop again
        #         2nd loop:  1(1,5,3)   2(2,4)
        #         3rd loop:  1(1,5,3,2,4)       right == 0
        while right > 0:
            lists[left] = mergeTwoLists(lists[left], lists[right])
            left += 1
            right -= 1
            if left >= right:
                left = 0
        return lists[0]