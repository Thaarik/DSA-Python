'''
797. All Paths From Source to Target
Medium
6.7K
137
Companies
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0]]
        result=[]
        n=len(graph)
        while stack:
            node = stack.pop()
            if node[-1]==n-1: # if the last element of the node list == n-1 
                result.append(node)
            else:
                for i in graph[node[-1]]: # for every element inside the node presenet in the graph of last element of the node list's index
                        stack.append(node+[i]) #append it
        return result
                
''' Example:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

how?: 
s=[[0]]
node = [0]
not 0 equal to n-1 (3)
so s = [[0,1],[0,2]]

node = [0,2]
not 2 equal to n-1 (3)
so s=[[0,1],[0,2,3]]

node = [0,2,3]
3 equal to n-1(3)
so result = [[0,2,3]]
s = [[0,1]]

node = [0,1]
not 1 equal to n-1 (3)
so s=[[0,1,3]]

node = [0,1,3]
3 equal to n-1(3)
so result = [[0,2,3].[0,1,3]]
s = []

return result
'''


