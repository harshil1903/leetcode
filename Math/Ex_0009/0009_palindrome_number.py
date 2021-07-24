
# 9. Palindrome Number
#
# Source : https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.



class Solution:
    def isPalindrome(self, x):
        return int(str(abs(x))[::-1]) == x


if __name__ == '__main__':
    s = Solution();

    print(s.isPalindrome(121))
    print(s.isPalindrome(123))