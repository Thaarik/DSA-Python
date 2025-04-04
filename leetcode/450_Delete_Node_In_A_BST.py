# 450. Delete Node in a BST
# Solved
# Medium
# Topics
# Companies
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            #  Find minimum in right sub tree
            currentNode = root.right
            while currentNode.left:
                currentNode = currentNode.left
            root.val = currentNode.val
            root.right = self.deleteNode(root.right,root.val)
        return root

# Delete Node from BST - O(H) time where H is tree height
# Steps:
# 1. If tree is empty, return the empty tree
# 2. Recursively search for node to delete:
#    - If key > current node's value, delete from right subtree
#    - If key < current node's value, delete from left subtree
# 3. When node is found (current node's value == key):
#    - Case 1: Node has no left child, replace with right child
#    - Case 2: Node has no right child, replace with left child
#    - Case 3: Node has both children:
#      a. Find successor (minimum value in right subtree)
#      b. Replace current node's value with successor's value
#      c. Delete the successor from right subtree
#
# Visual explanation:
#   Delete node 10:         20                  20
#                          /  \                /  \
#                        10    30     =>     15    30
#                       /  \                /
#                      5    15             5
#                          
#   Steps for node with both children:
#   1. Find min value in right subtree (15)
#   2. Replace 10's value with 15
#   3. Delete the original 15 node in right subtree


