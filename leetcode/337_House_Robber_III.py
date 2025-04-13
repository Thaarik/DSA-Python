'''
337. House Robber III
Solved
Medium
Topics
Companies
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # return [maxValueWithRoot, maxValueWithoutRoot]
        # maxValueWithRoot = node.val + leftSubTree[1] + rightSubTree[1] # Considering root and not considering left and right child
        # maxValueWithoutRoot = max(leftSubTree)+max(rightSubTree) # Considering left and right child by getting max of left and right subtree
        # maxValue = max(maxValueWithRoot, maxValueWithoutRoot)
        def dfs(node):
            if not node:
                return [0,0]
            leftSubTree = dfs(node.left)
            rightSubTree=dfs(node.right)
            maxValueWithRoot = node.val + leftSubTree[1] + rightSubTree[1] # Considering root and not considering left and right child
            maxValueWithoutRoot = max(leftSubTree)+max(rightSubTree) # Considering left and right child by getting max of left and right subtree
            return [maxValueWithRoot, maxValueWithoutRoot]
        return max(dfs(root))
    


# House Robber III - Binary Tree DFS with DP
#
# Time Complexity: O(n) where n is the number of nodes
# Space Complexity: O(h) where h is the height of the tree (recursion stack)
#
# Problem:
# - Tree represents houses with money (node.val)
# - Cannot rob two directly connected houses
# - Find maximum amount that can be robbed
#
# Approach:
# - Use bottom-up DP with post-order traversal
# - For each node, compute two values:
#   1. Max money if we rob this node (can't rob children)
#   2. Max money if we skip this node (can rob children)
#
# Explanation:
# - dfs returns [rob_this, skip_this]
# - rob_this = node.val + sum of skip_this from both children
# - skip_this = max possible value from each child
#
# Example:
#     3
#    / \
#   2   3
#    \   \
#     3   1
#
# For leaf node 3: [3, 0]
# For node 2: With=2+0+0=2, Without=max(0)+max(3,0)=3 -> [2, 3]
# For root: With=3+3+1=7, Without=max(2,3)+max(3,1)=6 -> [7, 6]
# Answer: max(7, 6) = 7

