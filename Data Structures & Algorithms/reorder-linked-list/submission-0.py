# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None


        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        r = prev

        i = 0
        prev = None
        z = head
        while z is not None and r is not None:
            if i % 2 == 0:
                temp = z.next
                z.next = r
                prev = r
                z = z.next
                r = r.next
            else:
                z.next

            i += 1


       
                

        
        