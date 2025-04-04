# 701. Insert into a Binary Search Tree
# Solved
# Medium
# Topics
# Companies
# You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

# Example 1:


# Input: root = [4,2,7,1,3], val = 5
# Output: [4,2,7,1,3,5]
# Explanation: Another accepted tree is:

# Example 2:

# Input: root = [40,20,60,10,30,50,70], val = 25
# Output: [40,20,60,10,30,50,70,null,null,25]
# Example 3:

# Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
# Output: [4,2,7,1,3,5]
 

# Constraints:

# The number of nodes in the tree will be in the range [0, 104].
# -108 <= Node.val <= 108
# All the values Node.val are unique.
# -108 <= val <= 108
# It's guaranteed that val does not exist in the original BST.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Recursive Approach
        # if not root:
        #     return TreeNode(val)
        # if val > root.val:
        #     root.right = self.insertIntoBST(root.right, val)
        # else:
        #     root.left = self.insertIntoBST(root.left, val)
        # return root
        
# Insert into Binary Search Tree - O(H) time where H is tree height
# Steps:
# 1. If tree is empty, create new node with value and return
# 2. If value > current node's value, recursively insert into right subtree
# 3. If value <= current node's value, recursively insert into left subtree
# 4. Return the modified root to maintain parent-child connections
# Note: Duplicates are inserted to left subtree in this implementation


        # Iterative Approach
        if not root:
            return TreeNode(val)
        currentNode = root
        while True:
            if val > currentNode.val:
                if not currentNode.right:
                    currentNode.right = TreeNode(val)
                    return root
                currentNode = currentNode.right
            else:
                if not currentNode.left:
                    currentNode.left = TreeNode(val)
                    return root
                currentNode = currentNode.left

# Insert into Binary Search Tree - Iterative Approach - O(H) time
# Steps:
# 1. If tree is empty, return new node with given value
# 2. Start traversal from root with a current node pointer
# 3. If value > current node's value:
#    - If right child exists, move to right child
#    - If no right child, create new node as right child and return
# 4. If value <= current node's value:
#    - If left child exists, move to left child
#    - If no left child, create new node as left child and return
# Note: Duplicates go to left subtree; approach uses O(1) space