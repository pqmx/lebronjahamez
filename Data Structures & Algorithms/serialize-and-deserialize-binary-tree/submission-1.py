# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        cur = root
        if cur is None:
            return ""

        queue = deque([cur])
        res = str(cur.val) + "#"
        while queue:
            node = queue.popleft()
            if node.left is None:
                res += "N#"
            else:
                res += str(node.left.val) + "#"
                queue.append(node.left)
            
            if node.right is None:
                res += "N#"
            else:
                res += str(node.right.val) + "#"
                queue.append(node.right)
        
        
        return res[:-1]
                

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        data = data.split("#")
        data = deque(data)
        
        head = None

        n = data.popleft()
        node = TreeNode(n)
        q = deque([node])
        
        while data:
            node = q.popleft()
            if head is None:
                head = node
            l = data.popleft()
            r = data.popleft()

            if l != "N":
                left = TreeNode(int(l))
                node.left = left
                q.append(left)
            else:
                node.left = None
            
            if r != "N":
                right = TreeNode(int(r))
                node.right = right
                q.append(right)
            else:
                node.right = None
        
        return head
            
            
            

            
        

        
            

        