
# 763. Partition Labels
#
# Source : https://leetcode.com/problems/partition-labels/
#
# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
#
# Return a list of integers representing the size of these parts.



from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        lookup = {}
        for i, char in enumerate(s):
            lookup[char] = i

        first, last = 0, 0
        result = []
        for i, char in enumerate(s):
            last = max(last, lookup[char])
            if i == last:
                # we reached the right most index
                result.append(i - first + 1)
                first = i + 1
        return result


if __name__ == '__main__':
    s = Solution();

    print(s.partitionLabels("ababcbacadefegdehijhklij"))