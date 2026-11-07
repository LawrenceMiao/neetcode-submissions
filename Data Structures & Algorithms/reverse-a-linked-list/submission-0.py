# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        behind = None
        current = head
        while True:
            next_node = current.next
            if next_node == None:
                current.next = behind
                return current
            current.next = behind
            behind = current
            current = next_node

