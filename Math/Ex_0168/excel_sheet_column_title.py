
# 168. Excel Sheet Column Title
#
# Source : https://leetcode.com/problems/excel-sheet-column-title/
#
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
#
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...



class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result, col = "", columnNumber

        while int(col) != 0:
            result += chr(int((col - 1) % 26) + 65)
            col = (col - 1) / 26

        return result[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(523482374))