'''
230. Kth Smallest Element in a BST
Solved
Medium
Topics
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # arr = []
        # def inorder(node, k):
        #     if not node:
        #         return
        #     inorder(node.left,k)
        #     arr.append(node.val)
        #     inorder(node.right,k)
        # inorder(root, k)       
        # return arr[k-1]

        # Recursive approach ( BFS):
        #  This approach uses the property that inorder traversal 
# of BST visits nodes in sorted order:
#
#        5
#      /   \
#     3     7
#    / \   / \
#   2   4 6   8
#
# Inorder traversal: [2, 3, 4, 5, 6, 7, 8]
# For k=3, kth smallest = 4
#
# Steps:
# 1. Initialize empty array to store values
# 2. Perform inorder traversal (left→root→right)
#    - Recursively traverse left subtree
#    - Add current node's value to array
#    - Recursively traverse right subtree
# 3. Return the (k-1)th element of array (0-indexed)
#
# Note: This approach uses O(n) extra space to store all values.

        stack = []
        result = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            if len(result)==k:
                return result[k-1]
            curr=curr.right
        
    #  Iterative approach (DFS):
    #  This approach uses a stack to perform an iterative inorder traversal of the BST:
    #  Steps:
    # 1. Initialize an empty stack and a variable to keep track of the current node
    # 2. Traverse the tree using a while loop:  
    #   - Push all left children of the current node onto the stack
    #   - Pop the top node from the stack and add its value to the result list
    #   - If the result list has k elements, return the kth smallest element
    # 3. Move to the right child of the popped node
    # 4. Repeat until the stack is empty or the kth smallest element is found
    # 5. Time complexity: O(n), where n is the number of nodes in the tree
    # 6. Space complexity: O(h), where h is the height of the tree (for the stack)
    
                
            