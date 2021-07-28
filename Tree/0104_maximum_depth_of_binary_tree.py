
# 104. Maximum Depth of Binary Tree
#
# Source : https://leetcode.com/problems/maximum-depth-of-binary-tree/
#
# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        return max(l, r)


# Input: root = [3,9,20,null,null,15,7]
# Output: 3