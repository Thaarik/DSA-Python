""" 
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false 

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        # create counts for s1 and s2 of length 26
        s1Count = [0]*26
        s2Count = [0]*26

        # fill the s1Count, s2Count element 1 when they are equal to alphabetical order of s1 and s2 with s1 length so that we can construct a sliding window

        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')]+=1
            s2Count[ord(s2[i])-ord('a')]+=1
        
        # create match counter to check whether they match all 26 alphabets in those 2 counters
        matches = 0
        for i in range(26):
            if(s1Count[i]==s2Count[i]):
                matches+=1
            
        
        # create sliding window where the window length is equal to the length of s1
        left = 0
        for right in range(len(s1),len(s2)): 
            if matches == 26:
                return True
            
            # create index for right addition (sliding)
            rindex = ord(s2[right])-ord('a')
            s2Count[rindex]+=1
            if s1Count[rindex]==s2Count[rindex]:
                matches+=1
            elif s1Count[rindex]+1==s2Count[rindex]: #if the countvalue of s2Count become too large
                matches -=1
            
            # create index for left deletion (sliding)
            lindex = ord(s2[left])-ord('a')
            s2Count[lindex]-=1
            if s1Count[lindex]==s2Count[lindex]:
                matches+=1
            elif s1Count[lindex]-1==s2Count[lindex]:#if the countvalue of s2Count become too small
                matches-=1
            print(s1Count)
            print(s2Count)
            left+=1
        print(matches)
        return matches==26

            

        


