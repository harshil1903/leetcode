class Solution:
    def myAtoi(self, s: str) -> int:

        MAX = 2147483647
        MIN = -2147483648
        result = 0
        size = len(s)

        if not s:
            return result

        i = 0

        while i < size and s[i].isspace():
            i += 1

        if i == size:
            return result

        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        while i < size and '0' <= s[i] <= '9':
            result = result * 10 + int(s[i])
            i += 1

        if result > MAX and sign > 0:
            return MAX
        elif result > MAX and sign < 0:
            return MIN
        else:
            return sign * result

    def myAtoi1(self, s: str) -> int:

        MAX = 2147483647
        MIN = -2147483648

        s = s.strip()
        sign = 1
        if s == "":
            return 0
        elif s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]

        num = ""
        for l in s:
            if l.isdigit():
                num += l
            else:
                break

        if num != "":
            result = sign * int(num)
            if result > 0 and result > MAX:
                return MAX
            elif result < 0 and result < MIN:
                return MIN
            else:
                return result

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("words and 987"))
    print(s.myAtoi1("-91283472332"))