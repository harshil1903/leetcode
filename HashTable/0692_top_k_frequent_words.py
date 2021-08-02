
# 692. Top K Frequent Words
#
# Source : https://leetcode.com/problems/top-k-frequent-words/
#
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes
# first.



from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        candidates = count.keys()

        # sort the dictionary keys first by frequency of the words, then sort by the word itself
        # using lambda function in the 'key' parameter below
        # -count[x] means descending order of count,
        # x means sort by the alphabetical values of the words
        res = sorted(candidates, key=lambda x: (-count[x], x))

        return res[:k]


if __name__ == '__main__':
    s = Solution();

    print(s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4))