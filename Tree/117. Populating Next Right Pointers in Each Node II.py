"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # #BFS 是work的即使不是perfect的tree， 但不是space o（1）
        # if not root:
        #     return root
        
        # q = [[root]]

        # while q:
        #     level = []
        #     node_lst = q.pop()

        #     for i, n in enumerate(node_lst):
        #         if i > 0:
        #             n.next = node_lst[i-1]
        #         if n.right:
        #             level.append(n.right)
        #         if n.left:
        #             level.append(n.left)
        #     if level:
        #         q.append(level)
        
        # return root

        # space O(1)写法
        if not root:
            return root
        curr = root

        # 外层 向下走
        while curr:
            dummy = Node(0)
            tail = dummy

            # 内层 横向走
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next
            
            curr = dummy.next

        return root

        # 这里感觉是linkedlist的写法
        # 关于几个loop，想清楚行走方向，先横向在纵向
        # 在不确定起点的时候就加一个dummy，其实我是有intuition 的但我最好没想要读写分离用linkedlist方法，其实潜意识是有感觉的
        