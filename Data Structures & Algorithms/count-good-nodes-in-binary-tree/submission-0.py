# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNode(root, root.val)

    def goodNode(self, root, maxVal):
        if root is None:
            return 0
        
        isGood = 0
        if root.val >= maxVal:
            isGood += 1
            maxVal = root.val
        
        return isGood + self.goodNode(root.left, maxVal) + self.goodNode(root.right, maxVal)

            
            

            
            