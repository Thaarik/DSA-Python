'''
383. Ransom Note
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #if the ransomeNote count - magazine Count gives empty count, then we can say that all the characters present in ransomeNote are used so the result is true, else it returns false
        return not Counter(ransomNote) - Counter(magazine)
