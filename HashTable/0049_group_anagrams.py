
# 49. Group Anagrams
#
# Source : https://leetcode.com/problems/group-anagrams/
#
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams_dict, result = collections.defaultdict(list), []

        # sort the strings, use them as keys and add the strings matching to same keys in sorted form as values
        for s in strs:
            sorted_str = ("").join(sorted(s))
            anagrams_dict[sorted_str].append(s)

        # each key will have list of anagrams
        for anagram in anagrams_dict.values():
            result.append(anagram)

        return result

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:

        d = collections.defaultdict(list)

        for s in strs:
            k = "".join(sorted(s))
            d[k].append(s)

        return d.values()


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]));