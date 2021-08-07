
# 14. Longest Common Prefix
#
# Source : https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".



from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix1(self, strs: List[str]) -> str:

        # zip with one argument will create tuples with each tuple having ith letter of the word
        # a = ["flower", "flow", "flight"]
        # x = zip(*a)
        # for i in x:
        #     print(i)
        # OUTPUT :
        # ('f', 'f', 'f')
        # ('l', 'l', 'l')
        # ('o', 'o', 'i')
        # ('w', 'w', 'g')

        a = zip(*strs)
        res = ""
        for i in a:
            b = set(i)
            if len(b) == 1:
                res += i[0]
            else:
                break
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]));