
# 451. Sort Characters By Frequency
#
# Source : https://leetcode.com/problems/sort-characters-by-frequency/
#
# Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.



from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # most_common gives descending sorted list with tuples of value and count
        # eg : [('e', 2), ('t', 1), ('r', 1)]
        count = Counter(s).most_common()
        res = ""

        for i in range(len(count)):
            res += (count[i][0] * count[i][1])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("sfdfjfdfcrrsr"))