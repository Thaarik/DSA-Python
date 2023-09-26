'''
424. Longest Repeating Character Replacement
Solved
Medium
Topics
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # O(26.n)

        # count = {}
        # ans = 0
        # left=0
        # for right in range(len(s)):
        #     count[s[right]]=1+count.get(s[right],0)
        #     while (right-left+1)-max(count.values())>k:
        #         count[s[left]]-=1
        #         left+=1
        #     ans=max(ans,right-left+1)
        # return ans


        # O(n)
        
        count = {}
        ans = 0
        left=0
        maxf=0
        for right in range(len(s)):
            count[s[right]]=1+count.get(s[right],0)
            maxf=max(maxf,count[s[right]])
            while (right-left+1)-maxf>k:
                count[s[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
        return ans

''' Approach
1. Using Slidig Window Technique.
2. The main formula to use is to find the length of the sliding window i.e., right ointer-left pointer+1.
3. So, in the sliding window, calculate the frequency of alphabets and then, from the frequency value, check if the difference between the length of the siding window and the maximum frequency alphabet count is less than or equal to k. If it greater than k, then increment/ move the left pointer to the next element and reduce the value of the left pointers previous alphabet count to 1 in the counter.
4. By doing ths, calculate the maximum length of the sliding window and return it.
'''


                


            
        