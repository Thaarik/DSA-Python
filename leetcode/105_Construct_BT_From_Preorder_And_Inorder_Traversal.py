'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Solved
Medium
Topics
Companies
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        # Create a hashmap to quickly locate values in inorder traversal
        indices = {v:i for i,v in enumerate(inorder)}
        self.i=0  # Global pointer for preorder traversal
        
        def dfs(l,r):
            # Base case: invalid range
            if l>r:
                return None
                
            # Get current root from preorder and advance pointer
            root_val = preorder[self.i]
            self.i += 1
            root = TreeNode(root_val)
            
            # Find root position in inorder traversal
            mid = indices[root_val]
            
            # Recursively build left and right subtrees
            root.left = dfs(l, mid-1)   # Process everything left of root
            root.right = dfs(mid+1, r)  # Process everything right of root
            
            return root
            
        return dfs(0, len(inorder)-1)
    
    # Approach:
    # 1. Create a dictionary to store the indices of the inorder traversal.
    # 2. Initialize a variable to keep track of the current index in the preorder traversal.
    # 3. Define a recursive function to build the tree.
    # 4. In each recursive call:
    #    - If the left index is greater than the right index, return None.
    #    - Get the root value from the preorder traversal using the current index.
    #    - Increment the current index.
    #    - Create a new TreeNode with the root value.
    #    - Find the index of the root value in the inorder traversal using the dictionary.
    #    - Recursively build the left and right subtrees using the updated indices.
    # 5. Return the root node.
    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # Space Complexity: O(n), for the dictionary storing indices and the recursion stack.

    # Approach: Use preorder to identify roots and inorder to determine left/right subtrees
# Tips:
# - Preorder traversal (Root->Left->Right) always gives root nodes first
# - Inorder traversal (Left->Root->Right) helps identify what's in left vs right subtree
# - Create hashmap of inorder elements for O(1) lookups instead of O(n) linear search
# - Use a class variable pointer to track current position in preorder array
# - For each node in preorder:
#     1. Create tree node with current preorder value
#     2. Find its position in inorder array
#     3. Everything left of this position belongs in left subtree
#     4. Everything right of this position belongs in right subtree
# Time: O(n) - we visit each node once
# Space: O(n) - for recursion stack and hashmap