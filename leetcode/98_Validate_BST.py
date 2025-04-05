'''
98. Validate Binary Search Tree
Medium
14.1K
1.2K
Companies
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left,right):
            if not node:
                return True
            if not(node.val>left and node.val<right):
                return False
            return(valid(node.left,left,node.val) and valid(node.right,node.val,right))
        return valid(root,float('-inf'),float('inf'))
    
# Check Valid Binary Search Tree - O(n) time complexity
# 
# Approach: Use recursive validation with range constraints
# Each node must satisfy: left_bound < node.val < right_bound
#
# Examples of constraints:
#
#           5
#         /   \
#        3     7
#       / \   / \
#      2   4 6   8
#
# Node 5: (-∞ < 5 < ∞) ✓
# Node 3: (-∞ < 3 < 5) ✓
# Node 7: (5 < 7 < ∞) ✓
# Node 2: (-∞ < 2 < 3) ✓
# Node 4: (3 < 4 < 5) ✓
# Node 6: (5 < 6 < 7) ✓
# Node 8: (7 < 8 < ∞) ✓

# 
# Invalid example:
#           5
#         /   \
#        3     7
#       / \   / \
#      2   6 6   8
#          ↑
# Node 6 on right fails: Not (5 < 6 < 7) ✗
# Node 6 on left fails: Not (3 < 6 < 5) ✗
#
# Steps:
# 1. Begin validation at root with (-∞, ∞) range
# 2. For left child, update upper bound to parent's value
# 3. For right child, update lower bound to parent's value
# 4. Return false if any node violates its constraints

            

            