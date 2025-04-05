'''
1448. Count Good Nodes in Binary Tree
Solved
Medium
Topics
Companies
Hint
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

 

Example 1:



Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
Example 2:



Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 

Constraints:

The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0
            result=0
            if root.val >=maxVal:
                result=1
            maxVal = max(maxVal, root.val)
            result += dfs(root.right, maxVal) + dfs(root.left, maxVal)
            return result
        return  dfs(root, root.val)

# Approach:
# 1. We will use DFS to traverse the tree.
# 2. We will keep track of the maximum value seen so far in the path from the root to the current node.
# 3. If the current node's value is greater than or equal to the maximum value seen so far, we will increment the count of good nodes.
# 4. We will update the maximum value seen so far and continue traversing the left and right subtrees.
# 5. Finally, we will return the count of good nodes.
#
# Complexity Analysis:
# 1. Time Complexity: O(n), where n is the number of nodes in the tree. We are visiting each node once.
# 2. Space Complexity: O(h), where h is the height of the tree. This is the space used by the recursion stack.
            

