
# 1773. Count Items Matching a Rule
#
# Source : https://leetcode.com/problems/count-items-matching-a-rule/
#
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule
# represented by two strings, ruleKey and ruleValue.
#
# The ith item is said to match the rule if one of the following is true:
#
# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.



from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        if ruleKey == "type":
            index = 0
        elif ruleKey == "color":
            index = 1
        else:
            index = 2

        return sum([1 for item in items if item[index] == ruleValue])

    def countMatches1(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        c = 0

        if ruleKey == "type":
            for i in items:
                if ruleValue == i[0]:
                    c += 1

        if ruleKey == "color":
            for i in items:
                if ruleValue == i[1]:
                    c += 1

        if ruleKey == "name":
            for i in items:
                if ruleValue == i[2]:
                    c += 1

        return c

if __name__ == '__main__':
    s = Solution();
    print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
    print(s.countMatches1( [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))