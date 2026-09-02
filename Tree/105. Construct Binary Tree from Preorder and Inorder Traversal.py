# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first value of preorder traversal is root
        # Inorder guarantee the left substree goes left of the node and right tree goes right of the tree 
        
        if not preorder or not inorder:
            return None 
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx+1:]
        left_preorder = preorder[1:1+len(left_inorder)]
        right_preorder = preorder[1+len(left_inorder):]

        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)
        return root
