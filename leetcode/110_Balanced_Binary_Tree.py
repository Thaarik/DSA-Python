'''
110. Balanced Binary Tree
Easy
9.1K
515
Companies
Given a binary tree, determine if it is 
height-balanced
.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.height(root.left)-self.height(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    
    def height(self,root: Optional[TreeNode]) -> bool:
        if not root:
            return 0 
        left = self.height(root.left)
        right = self.height(root.right)
        return 1+max(left,right)

    
    '''Approach:
    1. define the height of the tree function 
    2. base case of the main func: if not root, return true 
    3. if the absolute diff between the height of two subtree is greater than 1, return false
    4. else recursively continue the comparision of heights of each nodes until it hits the leaf node carrying True value.
    '''

    #JavaScript
#     var isBalanced = function(root) {
#     function height(root){
#         if(!root){
#             return 0
#         }
#         return 1+Math.max(height(root.left),height(root.right))
#     }
#     if (!root){
#         return true;
#     }
#     if(Math.abs(height(root.left)-height(root.right))>1){
#         return false;
#     }
#     return isBalanced(root.left) && isBalanced(root.right);
# };