'''
701. Insert into a Binary Search Tree
Medium

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ''' Iterative approach '''
        # if not root:
        #     return TreeNode(val=val,left = None, right=None)
        # curr = root
        # prev = root
        # while curr:
        #     prev = curr
        #     if curr.val < val:
                
        #         curr = curr.right
        #     else:
        #         curr = curr.left
        # if prev.val < val:
        #     prev.right = TreeNode(val=val,left = None, right=None)
        # else:
        #     prev.left = TreeNode(val=val,left = None, right=None)
        # return root
        ''' Recursive Approach '''
        if not root:
            return  TreeNode(val)
        if root.val<val:
            root.right = self.insertIntoBST(root.right,val) # if the node reach the none position, we need to assign an new treenode with given value and assign it to root.right
        else:
            root.left = self.insertIntoBST(root.left,val) # if the node reach the none position, we need to assign an new treenode with given value and assign it to root.left
        return root #as per the question

