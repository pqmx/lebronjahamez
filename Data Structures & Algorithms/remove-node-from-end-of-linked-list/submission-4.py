# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #lets find the length
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next

        cur = head
        prev = None
        for i in range(size): 
            if i == (size - n): # we are at the node we want to delete.   1234 n = 2 4 - 2 = 2
                if prev is None:
                    if cur.next is None:
                        return None
                    else:
                        return cur.next
                else:
                    prev.next = cur.next
                    return head
            else:
                prev = cur
                cur = cur.next


