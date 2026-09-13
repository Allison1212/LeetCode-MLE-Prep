# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # # My solution O(N) time and space 
        # res = []

        # def in_traversal(root):
        #     if not root:
        #         return 
        #     in_traversal(root.left)
        #     res.append(root.val)
        #     in_traversal(root.right)
        
        # in_traversal(root)
        # return res[k-1]

        # Improve by early stop 
        self.count = 0
        self.res = None

        def in_traversal(root):
            if not root:
                return 
            in_traversal(root.left)
            self.count+=1
            if self.count == k:
                self.res = root.val
                return 
            in_traversal(root.right)
        
        in_traversal(root)
        return self.res
        