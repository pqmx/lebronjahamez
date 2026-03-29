# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax = float('-inf')
        self.maxPathSums(root, 0)
        return self.globalMax
    
    def maxPathSums(self, root: Optional[TreeNode], sum: int) -> int:
        if root is None:
            return 0  # null node contributes 0

        # recursively get left and right, ignoring negative contributions
        left = max(self.maxPathSums(root.left, 0), 0)
        right = max(self.maxPathSums(root.right, 0), 0)

        # combined sum for this node
        combinedSum = root.val + left + right
        self.globalMax = max(self.globalMax, combinedSum)

        # return only one branch upward
        return root.val + max(left, right)