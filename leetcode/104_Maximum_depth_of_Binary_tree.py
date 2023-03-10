'''
104. Maximum Depth of Binary Tree
Easy
10.3K
163
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''using BFFS by finding the length of levels in a tree'''
        # queue = []
        # result = []
        # queue.append(root)
        # while queue:
        #     level = []
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         if node:
        #             level.append(node)
        #             queue.append(node.left)
        #             queue.append(node.right)
        #     if level:
        #         result.append(level)
        # return len(result)
        ''' Recursive DFS -find the maximum depth in every sub tree'''
        # if not root:
        #     return 0
        # return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        ''' Iterative DFS using Stack '''
        stack = [[root,1]] # stack containing the root and its initial depth value
        result = 0
        while stack:
            node,depth = stack.pop() #pop the stack containing node and its root
            if node:
                result = max(result,depth) #check the depth value for result
                stack.append([node.left,depth+1]) #push the node's left and right child with increment in depth
                stack.append([node.right,depth+1])
                #repeat the process untill all children's child value is none
        return result