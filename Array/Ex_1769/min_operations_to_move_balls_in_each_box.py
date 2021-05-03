from typing import List


class Solution:

    # optimized
    def minOperations(self, boxes: str) -> List[int]:
        left_count, right_count, cost = 0, 0, 0
        n = len(boxes)
        result = [0] * n

        # counting cost of left to right shift
        for i in range(n):
            cost += left_count
            if (boxes[i] == "1"):
                left_count += 1
            result[i] += cost

        # counting cost of right to left shift
        cost = 0
        for i in range(n - 1, -1, -1):
            cost += right_count
            if (boxes[i] == "1"):
                right_count += 1
            result[i] += cost

        return result

    def minOperations1(self, boxes: str) -> List[int]:
        count = len(boxes)
        result = []

        for i in range(count):
            result.append(0);
            for j in range(count):
                if (boxes[j] != "0"):
                    result[-1] += abs(i - j)

        return result

    def minOperations2(self, boxes: str) -> List[int]:
        result = []

        active = [i for i in range(len(boxes)) if boxes[i] == "1"]

        for i in range(len(boxes)):
            result.append(0)
            result[-1] = sum([abs(i - j) for j in active])

        return result




if __name__ == '__main__':
    s = Solution()

    print(s.minOperations("001011"))
    print(s.minOperations1("001011"))
    print(s.minOperations2("001011"))