"""
349. Intersection of Two Arrays
Easy
4.8K
2.1K
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(list(set(nums1)))
        result = []
        for n in set(nums2):
            if self.binarySearch(nums1,n,0,len(nums1)-1):
                result.append(n)
        return result


    def binarySearch(self, l: List[int], target:int, start: int, end: int)-> bool:
        mid = start+(end-start)//2
        if start>end:
            return False
        if l[mid]==target:
            return True
        if l[mid]>target:
            return self.binarySearch(l,target, start, mid-1)
        else:
            return self.binarySearch(l,target, mid+1, end)
        