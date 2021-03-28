class Solution:
    def runningSum(self, nums):
        temp = 0
        l = []
        for i in nums:
            temp += i
            l.append(temp)

        return l

if __name__ == '__main__':
    s = Solution();
    print(s.runningSum([1,2,3,4]))
    print(s.runningSum([5,6,7]))
