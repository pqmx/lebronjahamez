# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def deleteNode(node, key):
            if not node:
                return None
            if key > node.val:
                node.right = deleteNode(node.right, key)
            elif key < node.val:
                node.left = deleteNode(node.left, key)
            else:
                if node.right is None:
                    return node.left
                
                if node.left is None:
                    return node.right

                successor = node.right
                while successor.left:
                    successor = successor.left
                
                
                node.val = successor.val
                node.right = deleteNode(node.right,node.val)




            return node 
            
        return deleteNode(root, key)
                


            
        