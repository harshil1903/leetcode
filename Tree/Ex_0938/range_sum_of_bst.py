
# 938. Range Sum of BST
#
# Source : https://leetcode.com/problems/range-sum-of-bst/
#
# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low,
# high].



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    #recursive
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:

        def helper(root):
            if root:
                if low <= root.val <= high:
                    self.sum += root.val
                if low < root.val:
                    helper(root.left)
                if high > root.val:
                    helper(root.right)

        self.sum = 0
        helper(root)
        return self.sum

    def rangeSumBST1(self, root: TreeNode, low: int, high: int) -> int:
        result = 0
        s = [root]
        while s:
            node = s.pop()
            if node:
                if low <= node.val <= high:
                    result += node.val
                if low < node.val:
                    s.append(node.left)
                if node.val < high:
                    s.append(node.right)
        return result


# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
