
# 19. Remove Nth Node From End of List
# Medium

# Given the head of a linked list, remove the nth node from the end of the list and return its head

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head==None:
            return
        currNode = head
        length=0
        while currNode!=None:
            length+=1
            currNode=currNode.next
        k = length-n
        count=0
        currNode = head
        prevNode = head
        if k==0:
            return head.next
        while k!=count:
            prevNode =currNode
            currNode = currNode.next
            count+=1
        prevNode.next = currNode.next
        return head
    
'''Another approach:
        dummy=ListNode(0,head)
        left=dummy
        right=head
        while n>0 and right:
            right=right.next
            n-=1
        
        while right: # like a sliding window
            left=left.next
            right=right.next
        
        left.next=left.next.next
        return dummy.next
'''        