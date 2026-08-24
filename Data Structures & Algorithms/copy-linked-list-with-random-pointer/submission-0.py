"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    
        nodes = dict()

        cur = head
        prev = None
        while cur is not None:
            #create new node.
            node = Node(cur.val)

            # connect prev node to new node.
            if prev is not None:
                prev.next = node
            
            # set as key.
            nodes[cur.val] = node
              
        
            prev = node # cur node to our prev
            cur = cur.next


        cur = head
        while cur is not None:

            if cur.random is None:
                nodes[cur.val].random = None
            else:
                nodes[cur.val].random = nodes[cur.random.val]
            cur = cur.next
        

        return nodes[head.val]
            

   

        



        


