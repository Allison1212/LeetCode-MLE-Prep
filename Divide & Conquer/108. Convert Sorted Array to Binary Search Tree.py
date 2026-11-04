# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)-1
        mid = left + (right-left)//2

        if right < left:
            return None

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


        # By select mid will make sure the left and right subtree have nearly same number of nodes
        # and the array already sorted so left subtree will always smaller then root and right always larger 
        # time complexity O(nlogn)
        # space comlexity O(n)， nums[:mid]会创建新数组
