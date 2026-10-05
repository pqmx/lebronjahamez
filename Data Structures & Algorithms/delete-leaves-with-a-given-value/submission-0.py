# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def isTarget(root, target):
            if root is None:
                return False

            if root.left is None and root.right is None and root.val == target:
                return True

            hadChild = False
            if isTarget(root.left, target):
                root.left = None
                hadChild = True
            elif isTarget(root.right, target):
                root.right = None
                hadChild = True
            

            if root.left is None and root.right is None:
                return True
            
            return False
            

        isTarget(root, target)
        return root
        # if we have no children return True
        