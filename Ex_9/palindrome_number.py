class Solution:
    def isPalindrome(self, x):
        return int(str(abs(x))[::-1]) == x


if __name__ == '__main__':
    s = Solution();

    print(s.isPalindrome(121))
    print(s.isPalindrome(123))