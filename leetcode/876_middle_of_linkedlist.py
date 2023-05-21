
# 876. Middle of the Linked List
# Easy

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        if head==None:
            return
        count=0
        temp = head
        while temp!=None:
            count+=1
            temp=temp.next
        middle = count//2
        count = 0
        while middle!=count:
            head = head.next
            count+=1
        return head
    
''' Another Approach using Two pointers'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        slow,fast = temp,temp
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow
'''
1. Take two pointer slow and fats.
2. for each iteration, slow should  take one step and the fast should take two steps.
3. So during their steps, when fast reach none or fast.next reaches none, the slow pointer will be at the middle of the linkedlist. 
4. return that slow pointer node.
'''