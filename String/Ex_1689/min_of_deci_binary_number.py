class Solution:
    def minPartitions(self, n: str) -> int:
        return max(list(n))

if __name__ == '__main__':
    s = Solution();
    print(s.minPartitions("546484687921"))