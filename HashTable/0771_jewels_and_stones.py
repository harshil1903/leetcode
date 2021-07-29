
# 771. Jewels and Stones
#
# Source : https://leetcode.com/problems/jewels-and-stones/
#
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type
# of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case-sensitive, so "a" is considered a different type of stone from "A".



class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0;
        for s in stones:
            if(s in jewels):
                count+=1
        return count


if __name__ == '__main__':
    s = Solution();
    print(s.numJewelsInStones("aA", "aAAbbb"))