"""
Number of Connected Components in an Undirected Graph
Solved 
There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Example 1:

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2

"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        def findParent(n):
            if n!=parent[n]:
                n=findParent(parent[n])
            return parent[n]
        
        def union(n1,n2):
            n1_parent = findParent(n1)
            n2_parent = findParent(n2)
            if n1_parent == n2_parent:
                return 0
        
            if rank[n1_parent]>rank[n2_parent]:
                rank[n1_parent]+=rank[n2_parent]
                parent[n2_parent]=n1_parent
            else:
                rank[n2_parent]+=rank[n1_parent]
                parent[n1_parent]=n2_parent
            return 1
        
        result = n
        for n1,n2 in edges:
            result -= union(n1,n2)
        return result
        

 # Number of Connected Components in an Undirected Graph (Union-Find Solution)
# Approach: Union-Find with Path Compression and Union by Rank
# Steps:
# 1. Initialize each node as its own component (n components total)
# 2. Process each edge, merging components
# 3. Each successful union decreases component count by 1
#
# Example: n=5, edges=[[0,1],[1,2],[3,4]]
#
# Initial state:
# - parent = [0,1,2,3,4]
# - rank = [1,1,1,1,1]
# - result = 5 (start with n components)
#
# Graph visualization:
#   0 -- 1 -- 2    3 -- 4
#
# Process:
# 1. Edge [0,1]:
#    - find(0) = 0, find(1) = 1
#    - Union: parent[0] = 1, rank[1] = 2
#    - Decrement result: 5-1 = 4
#    - parent = [1,1,2,3,4], rank = [1,2,1,1,1]
#
# 2. Edge [1,2]:
#    - find(1) = 1, find(2) = 2
#    - Union: parent[2] = 1, rank[1] = 3
#    - Decrement result: 4-1 = 3
#    - parent = [1,1,1,3,4], rank = [1,3,1,1,1]
#
# 3. Edge [3,4]:
#    - find(3) = 3, find(4) = 4
#    - Union: parent[3] = 4, rank[4] = 2
#    - Decrement result: 3-1 = 2
#    - parent = [1,1,1,4,4], rank = [1,3,1,1,2]
#
# Final result = 2 connected components
#
# Intuition:
# - Start with each node as its own component (n total)
# - Each time we union two nodes from different components:
#   - The two components merge into one
#   - Total component count decreases by 1
# - The union function returns 1 for successful unions, 0 otherwise
#
# Time: O(E*α(N)) where E is the number of edges and α is the inverse Ackermann function
#       - Practically, α(N) <= 5 for any reasonable input, so O(E)
#
# Space: O(N) for the parent and rank arrays


        