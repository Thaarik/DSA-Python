'''
23. Merge k Sorted Lists
Hard
17K
617
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
        
        while len(lists)>1: # while loop until the all lists got merged into one
            mergedLists = []
            for i in range(0, len(lists),2):
                list1 = lists[i]
                if i+1 <len(lists): #to avoid i going over the maximum index value of the lists/mergedlists
                    list2 = lists[i+1]
                else:
                    list2 = None
                mergedLists.append(self.mergeLists(list1,list2))
            lists = mergedLists
        return lists[0]
    
    def mergeLists(self, list1, list2):
        dummy = ListNode()
        temp = dummy
        while list1 and list2:
            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        return dummy.next


'''Approach:
1. Same like 21. Merge two sorted lists
2. Here we are applying the same process with divide and conquer method so that we can have the time complexity of O(n log k).
3. Split two lists inside the master list and perform merge linkedlist function until it becomes the single merged linked list.
'''