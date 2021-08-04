
# 187. Repeated DNA Sequences
#
# Source : https://leetcode.com/problems/repeated-dna-sequences/
#
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
#
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
#
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may
# return the answer in any order.



from collections import Counter
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dna = set()
        res = set()

        for i in range(len(s) - 9):
            temp = s[i:i + 10]
            if temp in dna:
                res.add(temp)
            else:
                dna.add(temp)
        return list(res)

    def findRepeatedDnaSequences1(self, s: str) -> List[str]:
        l, res = [], []
        if len(s) < 10:
            return []

        for i in range(len(s) - 9):
            l.extend([s[i:i + 10]])

        counter = Counter(l)

        for key, value in counter.items():
            if value > 1:
                res.append(key)

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));