# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)



# In a complete binary tree, every level is fully filled except possibly the last level, which is filled from left to right. You can use this property to count the nodes much faster than visiting every single one.
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
            
#         # Find the depth of the far-left path
#         left_depth = 1
#         left_node = root.left
#         while left_node:
#             left_node = left_node.left
#             left_depth += 1
            
#         # Find the depth of the far-right path
#         right_depth = 1
#         right_node = root.right
#         while right_node:
#             right_node = right_node.right
#             right_depth += 1
            
#         # If the depths are equal, it's a perfect binary tree.
#         # Total nodes = 2^height - 1
#         if left_depth == right_depth:
#             return (2 ** left_depth) - 1
            
#         # If they aren't equal, we recursively count the left and right subtrees
#         return 1 + self.countNodes(root.left) + self.countNodes(root.right)