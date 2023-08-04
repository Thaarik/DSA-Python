'''
21. Merge Two Sorted Lists
Easy

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy linkedlist node
        dummy = ListNode()
        #create a temp and do all the fnction into this
        temp = dummy

        while list1 and list2:

            if list1.val<=list2.val:
                temp.next=list1
                list1=list1.next
            else:
                temp.next=list2
                list2=list2.next
            temp=temp.next
        #if there is any list1 or list2 elements left
        if list1:
            temp.next=list1
        elif list2:
            temp.next=list2
        return dummy.next
    
''' Approach:
1. Create a dummy linkedlist and assign its head equal to temp .
2. while list 1 and list 2 contains elements, if a node in anyone of the list is smaller than the other, 
    assign temp.next to that list and the list = its list.next so that it moves to the next node. Also do temp = temp.next to progress to the next node.
3. After the while loop, if there is any nodes left in anone of the lists, link it to the resultant merged list. 
'''

# JavaScript
# var mergeTwoLists = function(list1, list2) {
    # //iterative
    # // let dummy = new ListNode();
    # // let temp = dummy;
    # // while(list1 && list2){
    # //     if(list1.val<=list2.val){
    # //         temp.next = list1;
    # //         list1=list1.next
    # //     }else if(list1.val>list2.val){
    # //         temp.next=list2;
    # //         list2=list2.next;
    # //     }
    # //     temp=temp.next;
    # // }
    # // if(list1){
    # //     temp.next=list1;
    # // }else if(list2){
    # //     temp.next=list2;
    # // }
    # // return dummy.next;

    # //recursion
#     if(!list1){
#         return list2;
#     }
#     if(!list2){
#         return list1;
#     }
#     if(list1.val<list2.val){
#         list1.next=mergeTwoLists(list1.next,list2);
#         return list1;
#     }else {
#         list2.next=mergeTwoLists(list1,list2.next);
#         return list2;
#     }
# };