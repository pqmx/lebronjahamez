# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""
        while l1 or l2:
            if l1 is not None:
                n1 += str(l1.val)
                n1 = n1.next
            if l2 is not None:

                n2 += str(l2.val)
                n2 = n2.next
        
        value = str(int(reversed(n1))+ int(reversed(n2)))

        root = None
        head = None
        for n in value:
            if root is None:
                root = ListNode(int(n))
                head = root
            else:
                root.next = ListNode(int(n))
                root = root.next
        return head

        