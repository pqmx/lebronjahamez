# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indict = {n : i for i, n in enumerate(inorder)}
        p = 0


        def dfs(left, right):
            nonlocal p
        
            if left > right:
                return None
            


            root = TreeNode(preorder[p])
            mid = indict[preorder[p]]
            p += 1
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)


            return root
        
        
        return dfs(0, len(preorder) - 1)
                


        
            
            
            

            