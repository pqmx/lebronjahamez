# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def removeLeafNodes(root):
            if root is None:
                return None
            root.left = removeLeafNodes(root.left)
            root.right = removeLeafNodes(root.right)


            if root.left is None and root.right is None and root.val == target:
                return None
            
            return root
        return removeLeafNodes(root)
        # if we have no children return True
        