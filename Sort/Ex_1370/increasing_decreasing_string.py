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