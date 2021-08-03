
# 22. Generate Parentheses
#
# Source : https://leetcode.com/problems/generate-parentheses/
#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def generateParenthesisRecu(left, right, curr, result):
            if left == 0 and right == 0:
                result.append("".join(curr))
            if left > 0:
                curr.append('(')
                generateParenthesisRecu(left - 1, right, curr, result)
                curr.pop()
            if left < right:
                curr.append(')')
                generateParenthesisRecu(left, right - 1, curr, result)
                curr.pop()

        result = []
        generateParenthesisRecu(n, n, [], result)
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(4));