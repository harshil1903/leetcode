
# 5. Longest Palindromic Substring
#
# Source : https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, return the longest palindromic substring in s.


class Solution:

    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1),
                         expand(i, i + 2),
                         key=len)
        return result


    # referenced
    def longestPalindrome1(self, s: str) -> str:

        def expand(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return (right - left + 1) - 2

        left, right = -1, -2
        for i in range(len(s)):
            l = max(expand(s, i, i), expand(s, i, i + 1))
            if l > right - left + 1:
                right = i + l // 2
                left = right - l + 1
        return s[left:right + 1] if left >= 0 else ""


    # referenced
    def longestPalindrome2(self, s: str) -> str:

        if (not s):
            return []
        longest = [float("-inf"), 0, 0]

        def helper(start, end):
            while (start >= 0 and end < len(s) and s[end] == s[start]):
                start -= 1
                end += 1
            count = end - start - 1
            if (count > longest[0]):
                longest[0] = count
                longest[1] = start + 1
                longest[2] = end

        for i in range(len(s)):
            helper(i, i)
            helper(i, i + 1)
            if (longest[0] == len(s)):
                break

        return s[longest[1]: longest[2]]


if __name__ == '__main__':
    s = Solution();

    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome1("babad"))
    print(s.longestPalindrome2("babad"))