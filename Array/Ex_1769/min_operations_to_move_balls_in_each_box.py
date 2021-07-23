
# 1769. Minimum Number of Operations to Move All Balls to Each Box
#
# Source : https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
#
# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
#
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be
# more than one ball in some boxes.
#
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
#
# Each answer[i] is calculated considering the initial state of the boxes.



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