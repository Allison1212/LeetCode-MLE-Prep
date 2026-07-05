# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out_list = []

        def postorder(node):
            nonlocal out_list
            if not node:
                return out_list

            postorder(node.left)
            postorder(node.right)
            out_list.append(node.val)
        
        postorder(root)
        return out_list

    # Post-order: Left $\rightarrow$ Right $\rightarrow$ Root (Root is last/post)