"""
24. Swap Nodes in Pairs
Medium
10.5K
384
Companies
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        else:
            p1 = head
            p2 = head.next
            p1.next=self.swapPairs(p2.next)
            p2.next = p1   
            return p2

'''Approach
    1. Assign p1 = head and p2 = head .next
    2. since we need to swap pairs, i.e., a -> b -> c-> d to b->a->d->c , p1 = a and p2 = b. we call recursive function 
    for every p1.next i.e., a -> (next recursive function c -> d)
    3. After this recursive call we are swapping the pair p2 = b swapped to p1 = a i.e., b->a -> (recursive call resulting d->c) => b -> a ->d -> c
    4. we are returning p2 = b because of this order b -> a ->d -> c and the head beaing p2 = b

'''
