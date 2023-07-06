"""
547. Number of Provinces
Medium
8.5K
317
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [False]*len(isConnected) 

        def dfs(node):
            visited[node]=True
            for neighbor in range(len(isConnected)):
                    if isConnected[node][neighbor]==1 and not visited[neighbor]:
                        dfs(neighbor)

        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                provinces+=1

        return provinces
"""A depth-first search (DFS) algorithm to find the number of provinces in a given matrix representing connected cities.

Initialize the provinces variable to keep track of the number of provinces found.
Create a visited list to track the visited nodes. Initialize it with False for each node in the isConnected matrix.
Define a helper function dfs that takes a node as input and performs a depth-first search.
Within the dfs function:
a. Mark the current node as visited by setting visited[node] = True.
b. Iterate through the neighbors of the current node.
c. If the neighbor is connected (isConnected[i][neighbor] == 1) and it has not been visited, recursively call dfs on that neighbor.
Iterate through each node in the isConnected matrix using a for loop.
a. If the node has not been visited, call dfs on that node.
b. Increment provinces by 1 to count the province.
Return the provinces count.
Step-by-step execution with the given test case (isConnected = [[1,1,0],[1,1,0],[0,0,1]]):

Initialize provinces = 0.
Initialize visited = [False, False, False].
Start the first iteration with i = 0.
a. Since visited[0] is False, call dfs(0).
Mark visited[0] as True.
Iterate through neighbors (neighbor = 0, 1, 2):
For neighbor = 0, isConnected[0][0] is 1, but visited[0] is already True, so skip.
For neighbor = 1, isConnected[0][1] is 1, and visited[1] is False, so call dfs(1).
Mark visited[1] as True.
Iterate through neighbors (neighbor = 0, 1, 2):
For neighbor = 0, isConnected[1][0] is 1, and visited[0] is True, so skip.
For neighbor = 1, isConnected[1][1] is 1, but visited[1] is already True, so skip.
For neighbor = 2, isConnected[1][2] is 0, so skip.
For neighbor = 2, isConnected[0][2] is 0, so skip.
Move to the next iteration with i = 1.
Since visited[1] is True, skip.
Move to the last iteration with i = 2.
Since visited[2] is False, call dfs(2).
Mark visited[2] as True.
Iterate through neighbors (neighbor = 0, 1, 2):
For neighbor = 0, isConnected[2][0] is 0, so skip.
For neighbor = 1, isConnected[2][1] is 0, so skip.
For neighbor = 2, isConnected[2][2] is 1, but visited[2] is already True, so skip.
After all iterations, provinces = 2.
Return provinces as the output.
The given input isConnected = [[1,1,0],[1,1,0],[0,0,1]] represents three cities with connections. The algorithm finds that there are two provinces in the matrix.
"""




        