'''
26. Remove Duplicates from Sorted Array
Easy
10.9K
14.8K
Companies
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while i<=j and j<len(nums):
            if nums[i]!=nums[j]:
                nums[i+1]=nums[j]
                i+=1
            j+=1
        return i+1
    
'''
APPROACH:
1. Use Two pointer approach. initialize i=0,j=1.
2. while traversing, if nums[i] == nums[j], no need to change anything and just increment j.
3. if nums[i]!=nums[j], update the nexdt element of nums[i], i.e., nums[i+1] (both nums[i] and nums[i+1] are duplicates), equal to nums[j] having different ascending value. (So that all unique sorted value would be on the left and its duplicated on the right in the array.)
4. In the end just return i+1. that would be our k.
'''