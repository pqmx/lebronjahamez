# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l = head
        r = head
        while l is not None and r is not None:
            for i in range(2):
                r = r.next
                if r is None:
                    return False
            if l == r:
                return True      
            else:
                
                r = r.next
                l = l.next      
        
        return False
        


        