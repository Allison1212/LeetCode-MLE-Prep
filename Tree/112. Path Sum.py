# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        # base case: return cumulated sum == targetSum
        # Recursive case: dfs(root.left) | dfs(root.right)
        # return False

        # # My version
        # def dfs(node,curr_sum):
        #     if (not node.left) and (not node.right):
        #         return (curr_sum + node.val) == targetSum
        #     elif node.left and node.right: 
        #         return dfs(node.left,curr_sum+node.val) or dfs(node.right,curr_sum + node.val)
        #     elif node.left:
        #         return dfs(node.left,curr_sum+node.val)
        #     else:
        #         return dfs(node.right,curr_sum + node.val)
        
        # return dfs(root,0) if root else False

        # simplify
        

        def dfs(node,curr_sum):
            if not node:
                return False

            curr_sum += node.val
            if (not node.left) and (not node.right):
                return curr_sum == targetSum

            return dfs(node.left,curr_sum) or dfs(node.right,curr_sum)
        return dfs(root,0)

        # 注意base case的要求是leaf not null
        # time complexity O(n): 每个node 直走一次
        # space complexity O(h) 每一层是一个recursive call stack， h 是height


