# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        head = root
        def isTarget(cur, target):
            nonlocal head
            if cur is None:
                return False

            # we foudn our leaf node.
            if cur.left is None and cur.right is None and cur.val == target:
                return True

            hadChild = False



            # do we have parents st 
            if isTarget(cur.left, target):
                cur.left = None
                hadChild = True
            elif isTarget(cur.right, target):
                cur.right = None
                hadChild = True
            

            if cur.left is None and cur.right is None and hadChild and cur.val == target:
                if cur == head:
                    head = None
                return True
            
            return False
            

        isTarget(head, target)
        return head
        # if we have no children return True
        