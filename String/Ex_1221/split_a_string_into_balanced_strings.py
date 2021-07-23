
# 1221. Split a String in Balanced Strings
#
# Source : https://leetcode.com/problems/split-a-string-in-balanced-strings/
#
# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it in the maximum amount of balanced strings.
#
# Return the maximum amount of split balanced strings.



class Solution:
    def balancedStringSplit(self, s: str) -> int:

        result, count = 0, 0

        for c in s:
            if c == 'L':
                count += 1
            else:
                count -= 1

            if count == 0:
                result += 1

        return result

if __name__ == '__main__':
    s = Solution();
    print(s.balancedStringSplit("RLRRLLRLRL"))
    print(s.balancedStringSplit("RLRRRLLRLL"))