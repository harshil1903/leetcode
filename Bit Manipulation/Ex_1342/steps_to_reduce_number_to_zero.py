class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if(num % 2 == 0):
                num /= 2
            else:
                num -= 1
            count+=1
        return count

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(14))
    print(s.numberOfSteps(8))
    print(s.numberOfSteps(123))