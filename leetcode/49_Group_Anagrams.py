'''
49. Group Anagrams
Medium
16.9K
483
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs: 
            count=[0]*26
            for char in s:
                count[ord(char)-ord('a')]+=1
            ans[tuple(count)].append(s)

        return ans.values()

        # TC: O(m.n.26)

        # Create a hashmap that stores the count of each character in the string in the form of list containing 26 element with initial value as 0 as key and the strings that has equal counts as value. return those values. 
