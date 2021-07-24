
# 1880. Check if Word Equals Summation of Two Words
#
# Source : https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
#
# The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).
#
# The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted in to
# an integer.
#
# For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
# You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.
#
# Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.



class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        memo = {chr(ord("a") + i): str(i) for i in range(10)}

        first = int("".join([memo[char] for char in firstWord]))
        second = int("".join([memo[char] for char in secondWord]))
        target = int("".join([memo[char] for char in targetWord]))

        return first + second == target

    def isSumEqual2(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # ord('a') = 97

        first, second, target = 0, 0, 0
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
            target = target + ((ord(i) - 97) * 10 ** length)

        return first + second == target

if __name__ == '__main__':
    s = Solution();
    print(s.isSumEqual2("acb", "cba", "cdb"))
    print(s.isSumEqual("aaa", "a", "aab"))