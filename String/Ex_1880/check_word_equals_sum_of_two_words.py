class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        memo = {chr(ord("a") + i): str(i) for i in range(10)}

        first = int("".join([memo[char] for char in firstWord]))
        second = int("".join([memo[char] for char in secondWord]))
        target = int("".join([memo[char] for char in targetWord]))

        return first + second == target

    def isSumEqual2(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # ord('a') = 97

        first, second, third = 0, 0, 0
        length = len(firstWord)

        for i in firstWord:
            length -= 1
            first = first + ((ord(i) - 97) * 10 ** length)

        length = len(secondWord)

        for i in secondWord:
            length -= 1
            second = second + ((ord(i) - 97) * 10 ** length)

        length = len(targetWord)

        for i in targetWord:
            length -= 1
            third = third + ((ord(i) - 97) * 10 ** length)

        return first + second == third

if __name__ == '__main__':
    s = Solution();
    print(s.isSumEqual("acb", "cba", "cdb"))
    print(s.isSumEqual("aaa", "a", "aab"))