from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for x in encoded:
            result.append(result[-1] ^ x)
        return result

    def decode1(self, encoded: List[int], first: int) -> List[int]:
        result = [first]

        for num in encoded:
            temp = first ^ num
            result.append(temp)
            first = temp

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.decode([1,2,3],1))
    print(s.decode1([6,2,7,3],4))