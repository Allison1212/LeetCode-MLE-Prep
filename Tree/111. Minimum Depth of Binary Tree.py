# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        level = 0

        q = deque()

        if not root:
            return level
        else:
            q.append([root])
        
            while q:
                level_node = []
                node_lst = q.popleft()
                level = level + 1
                for n in node_lst:
                    if not n.right and not n.left:
                        return level
                    if n.left:
                        level_node.append(n.left)
                    if n.right:
                        level_node.append(n.right)
                q.append(level_node)
            
            return level