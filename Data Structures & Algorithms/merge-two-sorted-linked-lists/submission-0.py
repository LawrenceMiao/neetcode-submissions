# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val < list2.val:
            merged_list_head = list1
            list1 = list1.next
        else:
            merged_list_head = list2
            list2 = list2.next
        
        merged_list_tail = merged_list_head

        while True:
            if list1 is None:
                merged_list_tail.next = list2
                return merged_list_head
            
            if list2 is None:
                merged_list_tail.next = list1
                return merged_list_head

            if list1.val < list2.val:
                merged_list_tail.next = ListNode(list1.val)
                list1 = list1.next
            else:
                merged_list_tail.next = ListNode(list2.val)
                list2 = list2.next
            merged_list_tail = merged_list_tail.next
