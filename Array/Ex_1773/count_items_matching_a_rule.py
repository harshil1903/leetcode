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