# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        node = self.findRoot(root, subRoot)
        if node is None:
            return False
        return self.isSameTree(node, subRoot)

    def findRoot(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == subRoot.val:
            return root
        
        return self.findRoot(root.left, subRoot) or self.findRoot(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (q is None and p is not None):
            return False
        if p is None and q is None:
            return True
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)