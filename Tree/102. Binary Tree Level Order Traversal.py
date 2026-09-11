# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # # First attampt improve by remove list of list use variable reassignment, actually better then deque.
        res = []

        if not root:
            return res
        current_level = [root]
    
        while current_level:
            level = []
            res_level = []

            for n in current_level:
                res_level.append(n.val)
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
            if res_level:
                res.append(res_level)
            current_level = level
        return res

        # typical bfs, use deque 
        queue = deque()

        res = []

        queue.append(root)

        while queue:
            nbr_node = len(queue)
            res_level = []
            for _ in range(nbr_node):
                node = queue.popleft()
                # for the leave node that could be null add to the queue
                if node:
                    res_level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            if res_level:
                res.append(res_level)
        return res

        # deque 和用current_level两空间和时间复杂度都是o（n）



        
        # # Try recursive - recursive not good for bfs
        # res = []
        # if not root:
        #     return res
        
        # def bfs(current_level):
        #     next_level = []
        #     append_res = []
        #     if not current_level:
        #         return 

        #     for i in current_level:
        #         append_res.append(i.val)
        #         if i.left:
        #             next_level.append(i.left)
        #         if i.right:
        #             next_level.append(i.right)
        #     if append_res:
        #         res.append(append_res)
        #     return bfs(next_level)
        # bfs([root])
        # return res