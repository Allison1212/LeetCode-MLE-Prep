# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def help(root, left, right):
            if not root:
                return True
            else:
                if not (left < root.val < right):
                    return False
                return help(root.left, left, root.val) and help(root.right, root.val, right)
        
        return help(root,float('-inf'),float('inf'))
    
    # 不光root.left < root < root.right, left tree < right_tree
    # 当有left tree < right_tree 就该意识到point 之间的比较是不成立的了， 就要考了一个区间 - 全局意识， 减少if else
    # 少用self.res 这种外部的变量
   