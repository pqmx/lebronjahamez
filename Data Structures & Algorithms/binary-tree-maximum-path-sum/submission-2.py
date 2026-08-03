# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.maxPathSums(root, None);
    

    def maxPathSums(self, root: Optional[TreeNode], sum: int) -> int:
        if root is None:
            return 0
        if root.val < 0:
            if sum is None:
                return max(self.maxPathSums(root.left, sum), self.maxPathSums(root.right, sum), root.val)
            else:
                return max(sum, self.maxPathSums(root.left, sum), self.maxPathSums(root.right, sum), root.val)
        
        # root has to pos
        if sum is None: 
            sum = root.val
        else:
            sum += root.val
        left = self.maxPathSums(root.left, None)
        right = self.maxPathSums(root.right, None)
        #figure out any disconnection.

        if root.left is not None and root.left.val > 0:
            sum += left
        else: #left is negative
            if left > sum:
                sum = left


        if root.right is not None and root.right.val > 0:
            sum += right
        else: #right is negative
            if right > sum:
                sum = right
        
        return sum
        
