
# 20. Valid Parentheses
#
# Source : https://leetcode.com/problems/valid-parentheses/
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.



class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        brackets = { '(' : ')',
                     '{' : '}',
                     '[' : ']' }

        for i in s:
            # check if opening bracket or not
            if i in brackets:
                stack.append(i)

            # if closing bracket then check if stack empty or top of stack is complement to that of closing bracket
            elif len(stack) == 0 or brackets[stack.pop()] != i:
                return False

        return len(stack) == 0

    #referenced
    def isValid1(self, s: str) -> bool:

        pairs = []
        for c in s:
            if c in ('(', '{', '['):
                pairs.append(c)
            else:
                if len(pairs) == 0:
                    return False
                last = pairs.pop(-1)
                if (last == '(' and c != ')') or (last == '{' and c != '}') or (last == '[' and c != ']'):
                    return False
        if len(pairs) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{}[]()"));
    print(s.isValid("(()[)]"));