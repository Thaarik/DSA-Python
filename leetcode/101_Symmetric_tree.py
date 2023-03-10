'''
101. Symmetric Tree
Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def mirrorCheck (root1,root2):
            if root1 and root2: #if both child are none
                return (root1.val==root2.val) and mirrorCheck(root1.right,root2.left) and mirrorCheck(root1.left,root2.right)
            return root1 == root2 #if anyone or both are none, check whether they are symmetric because if  both children are None then None == None which is symmetric and returns true. Others are non-symmetric and returns false

        
        return mirrorCheck(root.left,root.right)
    