
# 107. Binary Tree Level Order Traversal II
#
# Source : https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
#
# Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).



from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        result, current = [], [root]

        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
        return result[::-1]


# Input: root = [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]