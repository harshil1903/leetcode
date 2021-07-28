
# 572. Subtree of Another Tree
#
# Source : https://leetcode.com/problems/subtree-of-another-tree/
#
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false
# otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a
# subtree of itself



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def areSame(first, second):
            if not first and not second:
                return True
            if not first or not second:
                return False

            if first.val == second.val:
                return areSame(first.left, second.left) and areSame(first.right, second.right)
            else:
                return False

        if not root:
            return False

        if areSame(root, subRoot):
            return True

        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True

        return False


# Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
# Output: false
#
# Input: root = [3,4,5,1,2], subRoot = [4,1,2]
# Output: true