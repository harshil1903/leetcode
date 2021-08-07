
# 125. Valid Palindrome
#
# Source : https://leetcode.com/problems/valid-palindrome/
#
# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.



class Solution:
    def isPalindrome(self, s: str) -> bool:
        # print(ord('A'), ord('Z'), ord('a'), ord('z'), ord('0'), ord('9'))
        # 65 90 97 122 48 57
        k = ""
        for i in s:
            if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
                k += i
            # convert capital letters into small
            elif 65 <= ord(i) <= 90:
                k += chr(ord(i) + 32)

        return k == k[::-1]

    def isPalindrome1(self, s: str) -> bool:

        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        stripped = ''.join(ch for ch in s.lower() if ch.isalnum())

        return stripped == stripped[::-1]

    def isPalindrome3(self, s: str) -> bool:
        stripped = [ch.lower() for ch in s if ch.isalnum()]

        return stripped == stripped[::-1]

    def isPalindrome4(self, s: str) -> bool:
        s = list(filter(str.isalnum, s.lower()))

        return s == s[::-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))