# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        current = head

        while current:
            n += 1
            current = current.next
            
        mid = n // 2

        current = head

        if n == 1:
            return None

        for _ in range(mid - 1):
            current = current.next
        current.next = current.next.next
        
        return head