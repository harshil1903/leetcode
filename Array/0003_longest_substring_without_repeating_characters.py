
# 3. Longest Substring Without Repeating Characters
#
# Source : https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Given a string s, find the length of the longest substring without repeating characters.



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        length = 0
        maxi = 0

        for i in range(len(s)):
            if s[i] not in sub:
                sub.append(s[i])
                length = length + 1
                if length > maxi:
                    maxi = length
            else:
                index = sub.index(s[i])

                sub = sub[index + 1:]
                sub.append(s[i])
                length = len(sub)

        return maxi

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("aab"))
    print(s.lengthOfLongestSubstring(""))