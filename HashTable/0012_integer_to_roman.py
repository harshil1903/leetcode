
# 12. Integer to Roman
#
# Source : https://leetcode.com/problems/integer-to-roman/
#
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as
# XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as
# IV.
# Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances
# where subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.



class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {1000:'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        res = ""
        for key in mapping:
            res += (num // key) * mapping[key]
            num = num % key
        return res

    def intToRoman1(self, num: int) -> str:
        number_map = {1: "I", 4: "IV", 5: "V", 9: "IX",
                      10: "X", 40: "XL", 50: "L", 90: "XC",
                      100: "C", 400: "CD", 500: "D", 900: "CM",
                      1000: "M"}
        keyset = sorted(number_map.keys())
        result = []

        while num > 0:
            for key in reversed(keyset):
                while int(num / key) > 0:
                    num -= key
                    result += number_map[key]

        return "".join(result)

    def intToRoman2(self, num: int) -> str:
        s = ''
        if num >= 1000:
            s += 'M' * (num // 1000)
            num %= 1000
        if num >= 900:
            s += 'CM'
            num %= 100
        if num >= 500:
            s += 'D' * (num // 500)
            num %= 500
        if num >= 400:
            s += 'CD'
            num %= 100
        if num >= 100:
            s += 'C' * (num // 100)
            num %= 100
        if num >= 90:
            s += 'XC'
            num %= 10
        if num >= 50:
            s += 'L' * (num // 50)
            num %= 50
        if num >= 40:
            s += 'XL'
            num %= 10
        if num >= 10:
            s += 'X' * (num // 10)
            num %= 10
        if num == 9:
            s += 'IX'
            num = 0
        if num >= 5:
            s += 'V' * (num // 5)
            num %= 5
        if num == 4:
            s += 'IV'
            num = 0
        s += 'I' * num
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(5485));