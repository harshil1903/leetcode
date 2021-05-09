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

if __name__ == "__main__":
    s = Solution()
    print(s.sortString("aaaabbbbcczpidjifzzzyyyzcc"))