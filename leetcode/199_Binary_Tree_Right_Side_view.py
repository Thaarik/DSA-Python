'''
199. Binary Tree Right Side View
Solved
Medium
Topics
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = []
        q.append(root)
        bfs = []
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            bfs.append(level)
        for i in range(len(bfs)):
            result.append(bfs[i].pop())
        return result
    

    # DFS approach
    # res = []

    #     def dfs(root, depth):
    #         if not root:
    #             return []
    #         if depth==len(res):
    #             res.append(root.val)
    #         dfs(root.right, depth+1)
    #         dfs(root.left, depth+1)
        
    #     dfs(root, 0)
    #     return res


# Approach
# 1. BFS
# 2. Traverse the tree level by level
# 3. Append the last element of each level to the result
# 4. Return the result
# 5. Time complexity: O(n)
# 6. Space complexity: O(n)

# 1. DFS
# 2. Traverse the tree depth by depth
# 3. Append the first element of each depth to the result
# 4. Return the result
# 5. Time complexity: O(n)
# 6. Space complexity: O(n)




