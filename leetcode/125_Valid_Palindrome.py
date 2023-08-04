'''
125. Valid Palindrome
Easy
6.8K
7K
Companies
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for character in s:
            if character.isalnum():
                newStr+=character.lower()
        text=list(newStr)
        left = 0
        right = len(text)-1
        while left<=right:
            if text[left]!=text[right]:
                return False
            left+=1
            right-=1
        return True

'''
Approach:
1. Two pointer approach
2. Remove the special characters in the string and convert the characters in the string into the lowercase.
3. Initialize left and right pointer starting from initial index and the end index respectively.
4. When the character in left and right index are not same, return False.
5. When they are same, just move on till the left and right pointer meets at the center and return true.
'''

#JavaScript
# var isPalindrome = function(s) {
#     let str = []
#         for(let i=0;i<s.length;i++){
#                 if(/[a-zA-Z0-9]/.test(s[i])){ // checks whether the char is alphabet or number
#                     str.push(s[i].toLowerCase())
#                 }
#         }
#         let left=0;
#         let right=str.length-1;
#         while(left<=right){
#             if(str[left]!==str[right]){
#                 return false;
#             }
#             left++;
#             right--;
#         }
#         return true;
# };