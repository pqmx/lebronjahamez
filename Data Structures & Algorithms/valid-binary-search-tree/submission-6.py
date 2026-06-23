# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validBST(root)
    def validBST(self, root: Optional[TreeNode], lower:int = float('-inf'), upper: int = float('inf')) -> bool:
        if root is None:
            return True
        
        if not (lower < root.val < upper):
            return False
        
        return self.validBST(root.left, lower, root.val) and self.validBST(root.right, root.val, upper)
            

