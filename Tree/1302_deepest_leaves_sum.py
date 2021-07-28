
# 1302. Deepest Leaves Sum
#
# Source : https://leetcode.com/problems/deepest-leaves-sum/
#
# Given the root of a binary tree, return the sum of values of its deepest leaves.



#Helper Class
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    #Referenced
    def deepestLeavesSum(self, root: TreeNode) -> int:

        level_nodes = [root]
        result = 0
        while level_nodes:
            temp_nodes = []      #Store all nodes 1 level below the current level_node
            result = 0
            for node in level_nodes:
                result += node.val
                if node.left is not None:
                    temp_nodes.append(node.left)
                if node.right is not None:
                    temp_nodes.append(node.right)
            level_nodes = temp_nodes
        return result

    #Referenced
    def deepestLeavesSum1(self, root: TreeNode) -> int:

        self.max_depth = self.find_max_depth(root)

        self.deepest_sum = 0
        self.get_deepest_sum(root, 1)

        return self.deepest_sum

    def get_deepest_sum(self, root, depth):
        if not root:
            return

        if not root.left and not root.right:
            if depth == self.max_depth:
                self.deepest_sum += root.val
            return

        self.get_deepest_sum(root.left, depth + 1)
        self.get_deepest_sum(root.right, depth + 1)

        return

    def find_max_depth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left = self.find_max_depth(root.left)
        right = self.find_max_depth(root.right)

        return max(left, right) + 1




if __name__ == '__main__':
    s = Solution()
    #Create a BTree of TreeNode type for input



