"""
684. Redundant Connection
Solved
Medium
Topics
premium lock icon
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]
        rank = [1]*(len(edges)+1)

        def find(n):
            if n!=parent[n]:
                parent[n]=find(parent[n])
            return parent[n]

        def union(n1,n2):
            n1_root, n2_root = find(n1), find(n2)
            if n1_root == n2_root:
                return False
            if rank[n1_root] > rank[n2_root]:
                parent[n2_root]=n1_root
                rank[n1_root]+=rank[n2_root]
            else:
                parent[n1_root]=n2_root
                rank[n2_root]+=rank[n1_root]
            return True
        
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
        return []
        

# Redundant Connection
# Approach: Union-Find with Path Compression and Union by Rank
# Steps:
# 1. Create a Union-Find data structure
# 2. Process edges one by one, attempting to union the nodes
# 3. If an edge connects two nodes already in the same set, it's redundant
#
# Example: edges = [[1,2],[1,3],[2,3]]
#
# Graph visualization:
#     1
#    / \
#   2---3
#
# Process:
# 1. Initialize parent = [0,1,2,3] and rank = [1,1,1,1]
#    Each node is its own parent, with rank 1
#
# 2. Process edge [1,2]:
#    - find(1) = 1, find(2) = 2
#    - Union: parent[1] = 1, parent[2] = 1
#    - parent = [0,1,1,3], rank = [1,2,1,1]
#
# 3. Process edge [1,3]:
#    - find(1) = 1, find(3) = 3
#    - Union: parent[3] = 1
#    - parent = [0,1,1,1], rank = [1,3,1,1]
#
# 4. Process edge [2,3]:
#    - find(2) = 1, find(3) = 1
#    - Same parent! This edge connects nodes already in the same set
#    - Return [2,3] as the redundant connection
#
# Intuition:
# - In a tree with n nodes, there should be exactly n-1 edges
# - If we have n edges (as in the problem), one edge is redundant
# - The Union-Find algorithm helps us find the first edge that creates a cycle
# - This works because we process edges in the given order
#
# Union-Find optimizations:
# 1. Path Compression: When finding a node's root, update its parent directly to the root
# 2. Union by Rank: Attach smaller trees under larger ones to minimize tree height
#
# Time: O(E*α(N)) where E is the number of edges and α is the inverse Ackermann function
#       - Practically, α(N) <= 5 for any reasonable input, so O(E)
#
# Space: O(N) for the parent and rank arrays