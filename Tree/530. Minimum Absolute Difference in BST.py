# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        prev_val = None

        def inorder(node):
            nonlocal min_diff,prev_val 
            if node.left:
                inorder(node.left)
            if prev_val is not None:
                min_diff = min(min_diff,abs(prev_val - node.val))
            prev_val = node.val
            if node.right:
                inorder(node.right)

        inorder(root)


        return min_diff

# BSF: left node value < root value < right node value 
# BSF: Inorder of BST produces sorted data
# Recursivly traverse left root and right 
# Time complexity: O(N)
# Space complexity O(H)