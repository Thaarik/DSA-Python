'''
206. Reverse Linked List
Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #just reverse the next links on each node and assign the head at the end node.
        prev = None
        while head:
            nextn = head.next
            head.next = prev
            prev = head
            head = nextn
        head = prev
        return head 
    
        '''recursive approach'''

        if not head :
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next=head
        head.next = None
        return newHead
