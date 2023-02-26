'''
350. Intersection of Two Arrays II
Easy
6.1K
831
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ''' answer for this problem and follow up 3 '''
        #using counter
        c = Counter(nums1)
        res = [] 
        print(c)
        for i in range(len(nums2)):
            if nums2[i] in c and c[nums2[i]] > 0: 
                res.append(nums2[i])
                c[nums2[i]] -= 1
        print(res)
        return res

        ''' answer for follow up 1,2 '''
        #using sort and two pointer
        
        # m = 0
        # n = 0
        # res = [] 
        # nums1, nums2 = sorted(nums1), sorted(nums2)

        # while m < len(nums1) and n < len(nums2): 
        #     if nums1[m] == nums2[n]: 
        #         res.append(nums1[m])
        #         m += 1
        #         n += 1

        #     else: 
        #         if nums1[m] < nums2[n]: 
        #             m +=1
        #         else: 
        #             n += 1
            
        # return res