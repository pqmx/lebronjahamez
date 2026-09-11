# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        hsh = {}


        for l in lists:
            cur = l
            while cur:
                if cur.val not in hsh:
                    hsh[cur.val] = []
                hsh[cur.val].append(cur)
                heapq.heappush(h, cur.val)
                cur = cur.next

        
        res = None
        prev = None
        while h:
            value = heapq.heappop(h)
            node = hsh[value].pop()
            if res is None:
                res = node
            

            node.next = None

            if prev:
                prev.next = node
            prev = node


        return res


            
            

            