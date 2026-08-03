# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root, root)
    def validBST(self, root: Optional[TreeNode], parent) -> bool:
        if root is None or parent is None:
            return True
        if root.left and root.left.val > root.val:
            return False
        if root.right and root.right.val < root.val:
            return False
        
        return self.validBST(root.left, root) and self.validBST(root.right, root) and self.validBST(root.left, parent) and self.validBST(root.right, parent)

