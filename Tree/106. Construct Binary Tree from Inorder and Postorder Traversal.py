# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Last node of postorder tree is always root

        # My recursive solution
        if not inorder or not postorder:
            return None 
        
        root = TreeNode(postorder[-1])

        # index() 会产生O(N^2)的时间复杂度
        root_idx = inorder.index(postorder[-1])

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx+1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]

        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)
        return root

        # O(N) solution
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) -1
        

        def help(idx_left, idx_right):
            
            if idx_left > idx_right:
                return None

            root = TreeNode(postorder[self.post_idx])
            root_idx = idx_map[postorder[self.post_idx]]
            self.post_idx-=1
            root.right = help(root_idx+1, idx_right)
            root.left = help(idx_left, root_idx-1)
            
            
            return root

        
        return help(0, len(postorder) -1)

        # recursive的写法已经切片法，传入2个已经切好的切片，所以左右顺序不重要
        # 但hashmap写法是公用一个postorder的index 那倒序就是root->right->left 顺序就重要了，因为取的node不一样
        # 然后在分左右的时候，起始左右点其实不用动，两段变短靠root的变化

