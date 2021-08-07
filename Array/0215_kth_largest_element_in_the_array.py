
# 215. Kth Largest Element in an Array
#
# Source : https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.



import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            heapq.heappushpop(heap, n)
        return heap[0]

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        n = sorted(nums, reverse=True)
        return n[k - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest( [3,2,3,1,2,4,5,5,6],4))