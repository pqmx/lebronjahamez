# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        insNode = TreeNode(val)


        def insertNode(root, val):
            if root is None:
                return False
            if root.val > val:
                if root.left is None:
                    root.left = insNode
                    return True
                else:
                    return insertNode(root.left, val)
                
            else:
                if root.right is None:
                    root.right = insNode
                    return True
                else:
                    return insertNode(root.right, val)


        head = root
        insertNode(head, val)
        return root


        