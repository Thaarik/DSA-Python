'''
543. Diameter of Binary Tree
Easy
11.6K
722
Companies
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # def dfs(root):
        #     nonlocal diameter
        #     if not root:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     diameter = max(left+right,diameter)
        #     return max(left,right)+1 
        # diameter = 0
        # dfs(root)
        # return diameter


        # '''Approach:
        # 1. create dfs function
        # 2. Base case: when root is none, return 0
        # 3. Take left sub tree and right sub tree
        # 4. find the diameter, i.e., maximum height of (previous left subtrees diameter + previous right subtrees ) or the previous diameter
        # 5. return the dfs with the height of the tree i.e., maximum of left or right subtree plus 1 (usual method of finding height of the tree)
        # 6. diameter value is initilized outside and records the maximum value. 
        # 7. Return that diameter value.
        #  '''

        '''Another approach '''
        if not root:
            return 0
        d1 = self.height(root.left)+self.height(root.right)
        d2 = self.diameterOfBinaryTree(root.left)
        d3 = self.diameterOfBinaryTree(root.right)
        
        return max(d1,max(d2,d3))

    # finding height of the tree
    def height(self, root:Optional[TreeNode])-> int:
        if not root:
            return 0
        return 1+ max(self.height(root.left),self.height(root.right))


        