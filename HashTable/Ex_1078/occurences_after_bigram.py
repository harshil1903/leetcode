from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        l = text.split()
        res = []
        if len(l) <= 2:
            return res

        for i in range(2, len(l)):
            if l[i - 2] == first and l[i - 1] == second:
                res.append(l[i])

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findOcurrences("alice is a good girl she is a good student", "a", "good"))