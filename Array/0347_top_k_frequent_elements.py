
# 347. Top K Frequent Elements
#
# Source : https://leetcode.com/problems/top-k-frequent-elements/
#
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        li = sorted(count, key=count.get, reverse=True)

        return li[:k]


    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        return [n for n, f in Counter(nums).most_common(k)]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1,1,3,4,2,3,1],2))