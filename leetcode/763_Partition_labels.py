'''
763. Partition Labels
Medium
9.5K
348
Companies
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {c: i for i,c in enumerate(s)}
        result = []
        size = 0
        end = 0
        for i,c in enumerate(s):
            size+=1
            end=max(lastIndex[c],end)
            if i==end:
                result.append(size)
                size=0
        return result
    

'''
1. We are finding each character's last index present in the input string and incrementing the size for each character traversal. 
   Once the traversed index is equal to the lastindex value, we are appending the size value inside the result, setting the size to 0 and continuing the partition process.
2. Create lastIndex dict containing the character as key and their last index as value. (for input:"ababcbacadefegdehijhklij" , the output of LastIndex is {'a': 8, 'b': 5, 'c': 7, 'd': 14, 'e': 15, 'f': 11, 'g': 13, 'h': 19, 'i': 22, 'j': 23, 'k': 20, 'l': 21})     
3. for each character and its index, we are incrementing the size and setting the end value which is the maximum value of lastIndex dict's value of the corresponding character and the previous end value.
4. if the index value is equal to the end value, the partition occurs as there are no characters present beyond the end index value. So we append the size into the result array and we set the size = 0.
5. The process continues till the end.
'''