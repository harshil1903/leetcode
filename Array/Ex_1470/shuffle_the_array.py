
# 1470. Shuffle the Array
#
# Source : https://leetcode.com/problems/shuffle-the-array/
#
# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].



class Solution:
    def shuffle(self, nums, n):
        ar = []
        for i in range(int(len(nums)/2)):
            ar.append(nums[i])
            ar.append(nums[int(len(nums)/2)+i])
        return ar

if __name__ == '__main__':
    s = Solution();

    print(s.shuffle([2,5,1,3,4,7], 3))
    print(s.shuffle([1,2,3,4,4,3,2,1], 4))