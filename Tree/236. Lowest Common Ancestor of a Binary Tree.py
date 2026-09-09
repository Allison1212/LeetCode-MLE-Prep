# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # First attempt
        if not root:
            return None
        
        if root == p or root == q:
            return root
        else: 
            l = self.lowestCommonAncestor(root.left, p, q)
            r = self.lowestCommonAncestor(root.right, p, q)

            if l and r:
                return root
            elif l:
                return l
            elif r:
                return r

# Optimal code:
        # 1. 递归终止条件
        if not root or root == p or root == q:
            return root
        
        # 2. 分治：去左右子树寻找 p 和 q
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # 3. 处理当前层逻辑
        if l and r:
            return root  # p 和 q 分别在两侧，当前节点就是最近公共祖先
        
        return l or r    # 如果一侧为空，说明两个节点都在另一侧，或者只找到了其中一个

    # 这题的要点是搞明白分类讨论情况
        # 可能性1: 一个可能性就是如果是left and right直接return root
        # 可能性2: 就是看两边subtree， 如果subtree 都return了值说明在树的两侧， return root
        #  可能性3: 两个点在一边，那就是一个是另一个的Ancestor