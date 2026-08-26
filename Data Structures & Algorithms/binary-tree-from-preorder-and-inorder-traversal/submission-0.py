# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        head = None
        indict = {n : i for i, n in enumerate(inorder)}
        visited = set()



        def dfs(p, cur):
            if p >= len(preorder):
                return
            if cur is None and p == 0: # starting.
                head = TreeNode(preorder[0])
                head = cur
                visited.add(preorder[0])


            if preorder[p] not in visited:
                visited.add(preorder[p])

            # find the number in inorder now go to the preceding.
            index = indict[preorder[p]]
            if index - 1 >= 0 and inorder[index - 1] not in visited:
                left = TreeNode(inorder[index - 1])
                cur.left = left
                dfs(p + 1, cur.left)
            
            if index + 1 < len(preorder) and inorder[index + 1] not in visited:
                right = TreeNode(inorder[index + 1])
                cur.right = right
                right = node(p + 2, cur.right)

        dfs(0, None)

        return head
            
            
            

            