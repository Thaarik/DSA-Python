
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
        """
        :type head: ListNode
        :rtype: ListNode
        """