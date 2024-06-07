# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        current = second_half
        prev = None

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next 
        second_half = prev

        maxV = 0
        while head and second_half:
            sumV = head.val + second_half.val
            maxV = max(sumV, maxV)
            head = head.next
            second_half = second_half.next

        return maxV