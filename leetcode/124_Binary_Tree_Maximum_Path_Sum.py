'''
124. Binary Tree Maximum Path Sum
Solved
Hard
Topics
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize with minimum possible value
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Get max path sum from left and right subtrees (ignore negative sums)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Calculate path sum through current node connecting left and right subtrees
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return maximum path sum starting from this node and going in one direction
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum
        

 
#   Binary Tree Maximum Path Sum
#   Time Complexity: O(n) where n is the number of nodes
#   Space Complexity: O(h) where h is the height of the tree (recursion stack)
 
#   Approach:
#   1. Use post-order traversal to process children before parent
#   2. For each node, compute two values:
#      a. Max path sum passing through this node (can form a complete path)
#      b. Max contribution this node can make to a path going upward
#   3. Keep track of global maximum path sum
 
#   Example tree:
#         -10
#         / \
#        9  20
#          /  \
#         15   7
 
#   Walkthrough:
#   - Process leaf node 15:
#     → max_gain(15) = 15
#     → max_sum = max(-∞, 15) = 15
  
#   - Process leaf node 7:
#     → max_gain(7) = 7
#     → max_sum = max(15, 7) = 15
  
#   - Process node 20:
#     → left_gain = max(max_gain(15), 0) = 15
#     → right_gain = max(max_gain(7), 0) = 7
#     → current_path_sum = 20 + 15 + 7 = 42
#     → max_sum = max(15, 42) = 42
#     → return 20 + max(15, 7) = 35
 
#   - Process leaf node 9:
#     → max_gain(9) = 9
#     → max_sum remains 42
 
#   - Process root node -10:
#     → left_gain = max(max_gain(9), 0) = 9
#     → right_gain = max(max_gain(20), 0) = 35
#     → current_path_sum = -10 + 9 + 35 = 34
#     → max_sum = max(42, 34) = 42
#     → return -10 + max(9, 35) = 25 (not used)
 
#   Final answer: 42 (path is 15 → 20 → 7)

