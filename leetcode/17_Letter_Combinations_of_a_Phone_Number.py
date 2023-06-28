"""
17. Letter Combinations of a Phone Number
Medium
15.4K
853
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"],
        }
        current = ""
        result = []

        def backtrack(digits,current,numberindex):
            if len(digits)==0:
                return result # if digits = "", then output = []
            if len(current)==len(digits):
                return result.append(current)
            for i in range(len(keypad[digits[numberindex]])):
                backtrack(digits,current+keypad[digits[numberindex]][i],numberindex+1)

        backtrack(digits,current,0)
        return result
                
     '''Approach:
        1. Backtracking 
        2. First create the keypad dict
        3. Follow the same backtrack template.
        4. For every list value present in each keypad key, call the backtrack function by appending the current value. The 'numberindex' denotes the index of key (number representation) of the keypad.
        5. when the len of current string = len of the given target, then append it into the result. This will be our base case
     '''   