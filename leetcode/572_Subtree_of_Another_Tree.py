'''
572. Subtree of Another Tree
Easy
7.3K
417
Companies
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False
        if self.isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right,q.right)
        return  (p.val==q.val) and left and right


    ''' Approach: 
    1. Same like isSame Tree
    2. except there is an edge case such as root = [1,1] and subroot = [1] -> this must return true
    3. so the main function edge case is if any one of root or subroot is none then return false.
    4. if isSametree func is true, return true.
    5. if not then skip and check on the subtrees of the root with the main function recursively. This will satisfy the step 2.
    '''