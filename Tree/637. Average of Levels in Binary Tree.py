# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        out = []

        if not root:
            return out
        else:
            queue = deque()
            queue.append(root)
            while queue:
                level = []
                level_size = len(queue)
                i = 0
                while i < level_size:
                    q = queue.popleft()
                    if q.left: 
                        queue.append(q.left)
                    if q.right: 
                        queue.append(q.right)
                    level.append(q.val)
                    i = i + 1
                out.append(sum(level)/level_size)
            return out

#BFS