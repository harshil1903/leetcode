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