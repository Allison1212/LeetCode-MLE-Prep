# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return []
        
        current_level = [root]
        reverse = False

        while current_level:
            level = []
            res_level = []

            for n in current_level:
                res_level.append(n.val)
                # deque 的写法需要if n，因为有可能没有left and right 
                # current写法不需要，因为如果空就不会进loop
                if n.left:
                    level.append(n.left)
                if n.right:
                    level.append(n.right)
            current_level = level

            if reverse:
                # res_level.reverse() in place 翻转比[::-1]（extra 空间） 要好
                res_level.reverse()
            res.append(res_level)
            reverse = not reverse
        return res
