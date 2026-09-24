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
                root = insNode
                return root
            if root.val > val:
                root.left = insertNode(root.left, val) 
            else:
                root.right = insertNode(root.right, val)
            return root
        insertNode(root, val)
        print(root.val)
        return root


        