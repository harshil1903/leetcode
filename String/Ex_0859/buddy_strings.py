class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        a = list(a)
        b = list(b)
        myset = set()
        size = len(a)
        diff = []
        if size != len(b):
            return False

        if a == b:
            for i in range(size):
                if (a[i] in myset):
                    return True
                myset.add(a[i])
        else:
            for i in range(len(a)):
                if (a[i] != b[i]):
                    diff.append(a[i])
                    diff.append(b[i])

            if len(diff) == 4 and diff[0] == diff[3] and diff[1] == diff[2]:
                return True

        return False

    def buddyStrings1(self, a: str, b: str) -> bool:
        a = list(a)
        b = list(b)
        myset = set()
        size = len(a)
        diff = []
        if size != len(b):
            return False

        if a == b and len(set(a)) < len(a):
            return True
        else:
            for i in range(len(a)):
                if (a[i] != b[i]):
                    diff.append((a[i], b[i]))

            if len(diff) == 2 and diff[0] == diff[1][::-1]:
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    print(s.buddyStrings("ab", "ab"))
    print(s.buddyStrings1("aa", "aa"))