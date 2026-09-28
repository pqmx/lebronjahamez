# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        cur = head
        prev = None
        while cur and left != cur.val:
            prev = cur
            cur = cur.next
        leftNode = cur
        leftPrev = prev

        # cur is our leftNode
        while cur and cur.val <= right:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        # prev should be our right node.
        rightNode = prev
        if leftPrev is None:
            head = rightNode
        else:
            leftPrev.next = rightNode
        leftNode.next = cur

        return head




        