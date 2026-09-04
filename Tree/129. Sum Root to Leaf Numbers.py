# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        # # My solution 
        # res = 0
        # if not root:
        #     return res
        # stack = [[root,str(root.val)]]

        # while stack:
        #     node_pair = stack.pop()
        #     node = node_pair[0]
        #     value = node_pair[1]

        #     if not node.left and not node.right:
        #         res+= int(value)
        #     if node.left:
        #         stack.append([node.left, value + str(node.left.val)])
        #     if node.right:
        #         stack.append([node.right, value + str(node.right.val)])
        # return res

        # After minor improve 
        res = 0
        if not root:
            return res
        stack = [[root,root.val]]

        while stack:
            node,value = stack.pop()

            if not node.left and not node.right:
                res+= value
            if node.left:
                stack.append([node.left, value * 10 + node.left.val])
            if node.right:
                stack.append([node.right, value * 10 + node.right.val])
        return res


        # 我和optimal的解法就差一个不会直接用十进制进位， str 是不可改变的每加一位都多存一次