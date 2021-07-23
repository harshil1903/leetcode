
# 171. Excel Sheet Column Number
#
# Source : https://leetcode.com/problems/excel-sheet-column-number/
#
# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...



class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for i in range(len(columnTitle)):
            result *= 26
            result += ord(columnTitle[i]) - ord('A') + 1
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("ARAMXEL"))