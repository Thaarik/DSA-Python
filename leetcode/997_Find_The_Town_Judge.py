'''
997. Find the Town Judge
Solved
Easy
Topics
Companies
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
'''

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0]*(n+1)
        for (a,b) in trust:
            count[a]-=1
            count[b]+=1
        for i in range(1,n+1):
            if count[i]==n-1:
                return i
        return -1

# Find the Town Judge
# Approach: Count Trusts (Indegree - Outdegree)
# Steps:
# 1. Create an array to track trust balance for each person (1 to n)
# 2. For each trust pair [a,b]:
#    - Decrement count for person a (they trust someone)
#    - Increment count for person b (they are trusted by someone)
# 3. The town judge must have a count of n-1 (trusted by everyone else, trusts nobody)
#
# Example with n=3, trust=[[1,3],[2,3],[3,1]]:
#
# Initial counts: [0, 0, 0, 0] (indices 0-3, ignore index 0)
#
# Process [1,3]: Person 1 trusts 3
#   - Decrement count[1]: [0, -1, 0, 0]
#   - Increment count[3]: [0, -1, 0, 1]
#
# Process [2,3]: Person 2 trusts 3
#   - Decrement count[2]: [0, -1, -1, 1]
#   - Increment count[3]: [0, -1, -1, 2]
#
# Process [3,1]: Person 3 trusts 1
#   - Decrement count[3]: [0, -1, -1, 1]
#   - Increment count[1]: [0, 0, -1, 1]
#
# Final counts: [0, 0, -1, 1]
# 
# For each person i (1 to 3):
#   - Person 1: count[1] = 0 ≠ n-1=2
#   - Person 2: count[2] = -1 ≠ n-1=2
#   - Person 3: count[3] = 1 ≠ n-1=2
#
# No one has count n-1, so return -1 (no judge).
#
# In a valid example with n=4, trust=[[1,4],[2,4],[3,4]]:
#   - Final counts would be: [0, -1, -1, -1, 3]
#   - Person 4 has count 3 (= n-1)
#   - Person 4 would be the judge
#
# Intuition: 
# - The judge is trusted by everyone (n-1 people) → +1 for each
# - The judge trusts nobody → no -1s
# - So judge's final count must be n-1
#
# Time: O(E + n) where E is the number of trust relationships
# Space: O(n) for the count array
