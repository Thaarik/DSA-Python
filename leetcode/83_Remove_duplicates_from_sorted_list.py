'''
83. Remove Duplicates from Sorted List
Easy

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''first approach with dummy'''

        # dummy = ListNode(next=head)
        # prev = dummy
        # curr = dummy.next
        # while curr and  curr.next :
        #     if curr.val==curr.next.val:
        #         curr=curr.next
        #         prev.next = curr
        #     else:
        #         prev=curr
        #         curr=curr.next
        # return dummy.next

        '''another approach without dummy'''
        curr = head
        while curr:
            while curr.next and curr.val==curr.next.val:
                #delete operation
                curr.next=curr.next.next
            curr=curr.next
        return head
