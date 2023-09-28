'''
143. Reorder List
Solved
Medium
Topics
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        firstHead = head

        # FInd the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        # Reverse the second half after splitting
        middle = slow.next
        slow.next=None # Splitting the second half of the list (Important)
        prev=None
        while middle:
            curr = middle
            middle=middle.next
            curr.next=prev
            prev=curr
        secondHead=prev

        # Link the two parts
        while secondHead: # usually second part of the linkedlist length is shorter than the first part
            tmp1, tmp2 = firstHead.next, secondHead.next
            firstHead.next = secondHead
            secondHead.next = tmp1
            firstHead, secondHead = tmp1, tmp2


        