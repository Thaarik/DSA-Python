# 557. Reverse Words in a String III
# Easy

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        res = []
        for i in range(len(l)):
            li = list(l[i])
            li = li[::-1]
            res.append("".join(j for j in li))
        return " ".join(r for r in res)