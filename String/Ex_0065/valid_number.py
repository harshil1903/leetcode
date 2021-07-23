
# 65. Valid Number
#
# Source : https://leetcode.com/problems/valid-number/
#
# A valid number can be split up into these components (in order):
#
# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components (in order):
#
# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# At least one digit, followed by a dot '.'.
# At least one digit, followed by a dot '.', followed by at least one digit.
# A dot '.', followed by at least one digit.
# An integer can be split up into these components (in order):
#
# (Optional) A sign character (either '+' or '-').
# At least one digit.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"],
# while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
#
# Given a string s, return true if s is a valid number.



import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))

    def isNumber1(self, s: str) -> bool:
        s = list(s)
        dot, exp, num, numAfterE = False, False, False, False

        for i in range(len(s)):
            if s[i].isdigit():
                num = True
            elif s[i] == ".":
                if dot or exp:
                    return False
                dot = True
            elif s[i] == "e" or s[i] == "E":
                if exp or not num:
                    return False
                exp = True
                num = False
            elif s[i] == "+" or s[i] == "-":
                if s[i - 1] != "e" and i != 0:
                    return False
            else:
                return False

        return num

if __name__ == "__main__":
    s = Solution()
    print(s.isNumber("564684"));
    print(s.isNumber1("6ee69"));