# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        out_list = []

        def preorder(node):
            nonlocal out_list
            if not node:
                return out_list
            out_list.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return out_list
    
    # Preorder: root -> left -> right