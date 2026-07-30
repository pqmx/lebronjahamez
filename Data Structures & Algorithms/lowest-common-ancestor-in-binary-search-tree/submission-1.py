# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            lg = p.val
            sm = q.val
        else:
            lg = q.val
            sm = p.val
        
        return self.low(root, lg, sm)

    
    def low(self, root, lg, sm):
        if root is None:
            return None
        
        #equal cases.
        if root.val == lg or root.val == sm:
            return root
        
        # go left
        if root.val > lg: 
            return self.low(root.left, lg, sm)
        elif root.val > sm: # greater than sm, smaller than lg -> we found
            return root
        else: # smaller than lg, smaller than sm
            return self.low(root.right, lg, sm)

        

            
        


            

        
        