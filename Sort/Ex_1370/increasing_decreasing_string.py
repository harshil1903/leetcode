
# 1370. Increasing Decreasing String
#
# Source : https://leetcode.com/problems/increasing-decreasing-string/
#
# Given a string s. You should re-order the string using the following algorithm:
#
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
#
#
# Return the result string after sorting s with this algorithm.



class Solution:
    def sortString(self, s: str) -> str:
        # ord('a') = 97

        result, count = [], [0] * 26

        for c in s:
            count[ord(c) - 97] += 1

        while len(result) != len(s):
            for c in range(len(count)):
                if not count[c]:
                    continue
                result.append(chr(97 + c))
                count[c] -= 1
            for c in reversed(range(len(count))):
                if not count[c]:
                    continue
                result.append(chr(97 + c))
                count[c] -= 1

        return "".join(result)

    def sortString1(self, s: str) -> str:
        res = ''
        dic = dict()
        lst = sorted(list(set(s)))
        for i in lst:
            dic[i] = s.count(i)
        while dic:
            tmp = lst[:]
            for i in lst:
                res += i
                dic[i] -= 1
                if dic[i] == 0:
                    dic.pop(i)
                    tmp.remove(i)
            lst = tmp
            lst.reverse()
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.sortString("aaaabbbbcczpidjifzzzyyyzcc"))
    print(s.sortString1("aaaabbbbcczpidjifzzzyyyzcc"))