"""
210. Course Schedule II
Solved
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        cycleDetect, visited = set(), set() # cycleDetect-> to detect a cycle, visited-> if the node is visited in the dfs, then that node is already captured and not needed so return true(like [] in course scheduler problem)
        output=[]

        for mainCourse, prerequisiteCourse in prerequisites:
            preMap[mainCourse].append(prerequisiteCourse)

        def dfs(course):
            if course in cycleDetect:
                return False
            if course in visited:
                return True
            
            cycleDetect.add(course)
            for prerequisiteCourse in preMap[course]:
                if not dfs(prerequisiteCourse):
                    return False
            cycleDetect.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output

# Course Schedule II
# Approach: DFS with Cycle Detection and Topological Sorting
# Steps:
# 1. Create an adjacency list representation (preMap)
# 2. Use DFS to detect cycles and build a topological ordering
# 3. Return the ordering if no cycle is found, else return empty list
#
# Example: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#
# Initial preMap:
# Course 0: [] (no prerequisites)
# Course 1: [0] (prerequisite: course 0)
# Course 2: [0] (prerequisite: course 0)
# Course 3: [1,2] (prerequisites: courses 1 and 2)
#
# Graph visualization:
#      0
#     / \
#    v   v
#    1-->3
#    ^  /
#    | /
#    2/
#
# Process:
# 1. Start DFS with course 0:
#    - Add 0 to cycleDetect = {0}
#    - No prerequisites, so add 0 to visited = {0}
#    - Add 0 to output = [0]
#
# 2. Start DFS with course 1:
#    - Add 1 to cycleDetect = {1}
#    - Check prerequisite 0 (already visited), return true
#    - Add 1 to visited = {0, 1}
#    - Add 1 to output = [0, 1]
#
# 3. Start DFS with course 2:
#    - Add 2 to cycleDetect = {2}
#    - Check prerequisite 0 (already visited), return true
#    - Add 2 to visited = {0, 1, 2}
#    - Add 2 to output = [0, 1, 2]
#
# 4. Start DFS with course 3:
#    - Add 3 to cycleDetect = {3}
#    - Check prerequisites 1 and 2 (already visited), return true
#    - Add 3 to visited = {0, 1, 2, 3}
#    - Add 3 to output = [0, 1, 2, 3]
#
# Final output = [0, 1, 2, 3]
#
# Note: There's an issue in the code - it's creating a reversed topological order.
# The correct order would be [3, 1, 2, 0] or [3, 2, 1, 0] since:
# - Course 0 must be taken first (has no prerequisites)
# - Courses 1 and 2 require course 0
# - Course 3 requires courses 1 and 2
#
# The preMap is actually recording the reverse of prerequisites - it maps courses to their 
# prerequisites rather than mapping courses to their dependent courses.
#
# Time: O(V + E) where V is the number of courses and E is the number of prerequisite pairs
# Space: O(V + E) for the adjacency list, visited set, and recursion stack
