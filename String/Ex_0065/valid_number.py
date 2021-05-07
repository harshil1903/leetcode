import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))

    def isNumber1(self, s: str) -> bool:
        s = list(s)
        dot, exp, num, numAfterE = False, False, False, False

        for i in range(len(s)):
            if s[i].isdigit():
                num = True
            elif s[i] == ".":
                if dot or exp:
                    return False
                dot = True
            elif s[i] == "e" or s[i] == "E":
                if exp or not num:
                    return False
                exp = True
                num = False
            elif s[i] == "+" or s[i] == "-":
                if s[i - 1] != "e" and i != 0:
                    return False
            else:
                return False

        return num

if __name__ == "__main__":
    s = Solution()
    print(s.isNumber("564684"));
    print(s.isNumber1("6ee69"));