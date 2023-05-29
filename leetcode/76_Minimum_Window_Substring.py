'''
76. Minimum Window Substring
Hard
15K
634
Companies
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # table =defaultdict(int)
        # currentres = ""
        # result = ""
        # minlen = math.inf
        # #form hashtable containing T value with its count.
        # for i in range(len(t)):
        #     table[t[i]]+=1
        # counter = len(table)
        # start=end = 0

        # #slide end pointer
        # while end<len(s):
        #     if s[end] in table:
        #         table[s[end]]-=1
        #         if table[s[end]]==0:
        #             counter-=1
        #     end+=1
        #     while counter==0:
        #         currentres = s[start:end]
        #         if len(currentres)<minlen:
        #             result = currentres
        #             minlen=len(currentres)
        #         if s[start] in table:
        #             table[s[start]]+=1
        #             if table[s[start]]>0:
        #                 counter+=1
        #         start+=1
        # return result

        '''Another approach'''
        if t == "":
            return ""

        tableT, tableS={},{}

        for c in t:
            tableT[c] = 1 + tableT.get(c,0) #if tableT[c] exists otherwise gives value 0
        
        res,resLen = [-1,-1], math.inf
        have,need =0,len(tableT)
        start = 0

        for end in range(len(s)):
            endChar = s[end]
            tableS[endChar] = 1+tableS.get(endChar,0)
            if endChar in tableT and tableS[endChar]==tableT[endChar]:
                have+=1

            while have == need:
                
                if (end-start+1)<resLen:
                    res = [start,end]
                    resLen = end-start+1
                startChar = s[start]
                tableS[startChar]-=1
                if startChar in tableT and tableS[startChar]<tableT[startChar]: #because we decrement the startChar, so tableS[startChar] will be less than the one in tableT[startChar]
                    have-=1
                start+=1
        if resLen!=math.inf:
            start,end = res
            return s[start:end+1]
        else:
            return ""



