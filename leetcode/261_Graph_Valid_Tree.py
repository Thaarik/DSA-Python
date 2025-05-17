"""
261. Graph Valid Tree - Explanation
Problem Link

Description
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2


Keyword arguments:
argument -- description
Return: return_description
"""

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
            
        # Build the adjacency list
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        # Keep track of visited nodes
        visited = set()
        
        def dfs(currentNode, previousNode):
            if currentNode in visited:
                return False
                
            visited.add(currentNode)
            
            for neighborNode in adj[currentNode]:
                # Skip the node we just came from
                if neighborNode == previousNode:
                    continue
                    
                # If we find a cycle or can't continue DFS, return False
                if not dfs(neighborNode, currentNode):
                    return False
                    
            return True
        
        # Start DFS from node 0 (any node would work)
        # Check if DFS succeeds and we visited all nodes
        return dfs(0, -1) and len(visited) == n

# Graph Valid Tree
# Approach: DFS with Cycle Detection
# Steps:
# 1. Check if the graph has exactly n-1 edges (property of a tree)
# 2. Build an adjacency list representation of the graph
# 3. Use DFS to check if:
#    - There are no cycles
#    - All nodes are connected
#
# Example with n=5, edges=[[0,1],[0,2],[0,3],[1,4]]:
#
# Initial adjacency list:
# Node 0: [1, 2, 3]
# Node 1: [0, 4]
# Node 2: [0]
# Node 3: [0]
# Node 4: [1]
#
# Graph visualization:
#     0
#    /|\
#   1 2 3
#   |
#   4
#
# Step 1: Check edges count
# - n = 5, so we need exactly n-1 = 4 edges
# - edges.length = 4 ✓
#
# Step 2: DFS to check for cycles and connectivity
# Start DFS at node 0:
# - Visit node 0, add to visited set: {0}
# - Process neighbors: 1, 2, 3
#   - Neighbor 1: Not visited, recursive DFS
#     - Visit node 1, add to visited set: {0, 1}
#     - Process neighbors: 0, 4
#       - Neighbor 0: Already visited, but it's the parent node, skip
#       - Neighbor 4: Not visited, recursive DFS
#         - Visit node 4, add to visited set: {0, 1, 4}
#         - Process neighbors: 1
#           - Neighbor 1: Already visited, but it's the parent node, skip
#         - All neighbors processed, return true
#     - All neighbors processed, return true
#   - Neighbor 2: Not visited, recursive DFS
#     - Visit node 2, add to visited set: {0, 1, 4, 2}
#     - Process neighbors: 0
#       - Neighbor 0: Already visited, but it's the parent node, skip
#     - All neighbors processed, return true
#   - Neighbor 3: Not visited, recursive DFS
#     - Visit node 3, add to visited set: {0, 1, 4, 2, 3}
#     - Process neighbors: 0
#       - Neighbor 0: Already visited, but it's the parent node, skip
#     - All neighbors processed, return true
# - All neighbors processed, return true
#
# Final visited set: {0, 1, 4, 2, 3}
# Visited nodes count = 5 = n ✓
#
# There are no cycles and all nodes are connected, so this is a valid tree.
#
# Key properties of a tree:
# 1. Exactly n-1 edges
# 2. No cycles
# 3. All nodes are connected
#
# Time: O(n + e) where n is the number of nodes and e is the number of edges
# Space: O(n + e) for the adjacency list and visited set

