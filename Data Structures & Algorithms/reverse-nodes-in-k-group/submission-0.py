# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # count length
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy
        cur = head

        for _ in range(size // k):
            group_start = cur

            # reverse k nodes
            prev = None
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # reconnect
            group_prev.next = prev
            group_start.next = cur

            # move forward
            group_prev = group_start

        return dummy.next