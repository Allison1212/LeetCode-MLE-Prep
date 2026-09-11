# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []

        node_list = [root]

        while node_list:
            level = []
            res.append(node_list[0].val)
            for i, v in enumerate(node_list):
                if v.right:
                    level.append(v.right)
                if v.left:
                    level.append(v.left)
            node_list = level
        
        return res