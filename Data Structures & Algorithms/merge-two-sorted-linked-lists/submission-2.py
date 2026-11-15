# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        if not list1 and not list2:
            return None

        if not list1:
            new_head = list2
            candidate1 = None
            candidate2 = list2.next

        if not list2:
            new_head = list1
            candidate1 = list1.next
            candidate2 = None

        if list1 and list2:
            if list1.val <= list2.val:
                new_head = list1
                candidate1 = new_head.next
                candidate2 = list2
            else:
                new_head = list2
                candidate1 = list1
                candidate2 = list2.next

        curr_node = new_head

        while candidate1 or candidate2:
            if not candidate2 or (candidate1 and candidate1.val <= candidate2.val):
                curr_node.next = candidate1
                curr_node = curr_node.next
                candidate1 = candidate1.next
            elif candidate2:
                curr_node.next = candidate2
                curr_node = curr_node.next
                candidate2 = candidate2.next

            

        return new_head
