from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        p = list(s)
        result = [""] * len(s)
        j = 0
        for i in indices:
            result[i] = p[j]
            j += 1

        return "".join(result)

    def restoreString1(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, ch in zip(indices, s):
            res[i] = ch
        return ''.join(res)

if __name__ == '__main__':
    s = Solution()
    print(s.restoreString("codeleet",[4,5,6,7,0,1,2,3]))
    print(s.restoreString1("codeleet",[4,5,6,7,0,1,2,3]))