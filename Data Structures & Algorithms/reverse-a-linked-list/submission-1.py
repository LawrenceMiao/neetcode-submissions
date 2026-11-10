# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        if curr_node is None:
            return None
        while True:
            
            if curr_node.next is None:
                curr_node.next = prev_node
                break
            next_node = curr_node.next
            if prev_node is None:
                curr_node.next = None
            else:
                curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            


        return curr_node
