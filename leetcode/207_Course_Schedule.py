'''
207. Course Schedule
Medium
14.5K
575
Companies
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course,prerequisite in prerequisites:
            preMap[course].append(prerequisite)
        visitedSet = set()
        def dfs(course):
            if course in visitedSet:
                return False
            if preMap[course]==[]:
                return True
            
            visitedSet.add(course)
            for i in preMap[course]:
                if not dfs(i):
                    return False
            visitedSet.remove(course)
            preMap[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
''' Approach
The code defines a function named canFinish which takes two parameters: numCourses (the total number of courses) and prerequisites (a list of prerequisite courses for each course). The function returns a boolean value indicating whether it is possible to finish all the courses.

The algorithm works as follows:

1. Create an empty dictionary preMap to store the prerequisites for each course. The keys of the dictionary are the course numbers, and the values are lists of prerequisite courses.
Iterate through the prerequisites list and populate the preMap dictionary with the prerequisite information for each course.
2. Create an empty set visitedSet to keep track of visited courses during the depth-first search (DFS) traversal.
Define a recursive helper function dfs that takes a course number as input and performs the DFS traversal to check if it is possible to finish that course.
3. In the dfs function:
        a. Check if the course is already in the visitedSet. If so, return False as it indicates a cycle in the course dependency graph, and it is not possible to finish the courses.
        b. Check if the course has no prerequisites (i.e., the preMap[course] list is empty). If so, return True as it indicates that the course can be finished.
        c. Add the current course to the visitedSet.
        d. Iterate through each prerequisite course for the current course and recursively call the dfs function on them. If any of the prerequisite courses cannot be finished (dfs returns False), return False as it indicates that the current course cannot be finished.
        e. Remove the current course from the visitedSet and set the preMap[course] list to empty, indicating that the course has been completed.
        f. Return True to indicate that the current course can be finished.
4. Iterate through each course number from 0 to numCourses - 1 and call the dfs function on each course.
5. If any course cannot be finished (dfs returns False), return False as it indicates that it is not possible to finish all the courses.
6. If all courses can be finished, return True.
7. The code essentially performs a DFS traversal on the course dependency graph and checks if there are any cycles or unresolved prerequisites. If there are no cycles and all prerequisites can be resolved, it returns True; otherwise, it returns False.
'''