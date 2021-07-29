
# 98. Validate Binary Search Tree
#
# Source : https://leetcode.com/problems/validate-binary-search-tree/
#
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTRecursive(root, float("-inf"), float("inf"))

    def isValidBSTRecursive(self, root, low, high):
        if root is None:
            return True

        return low < root.val < high \
               and self.isValidBSTRecursive(root.left, low, root.val) \
               and self.isValidBSTRecursive(root.right, root.val, high)


    #referenced keep pushing left node until none, then compare it to the right node first, then with it's root.
    def isValidBST1(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack, pre = [], None

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if pre and pre.val >= node.val:
                    return False
                pre = node
                root = node.right
        return True


# Input: root = [2,1,3]
# Output: true
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.