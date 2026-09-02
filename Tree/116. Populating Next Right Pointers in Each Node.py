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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # # My solution
        if not root:
            return None
        root.next = None
        queue = deque()
        queue.append([root])

        while queue:
            level = []
            node_lst = queue.popleft()
            for i, n in enumerate(node_lst):
                if i > 0:
                    n.next = node_lst[i-1]
                if n.right:
                    level.append(n.right)
                if n.left:
                    level.append(n.left)
            if level:
                queue.append(level)
        return root

        # Space O(1) Solution
        if not root:
            return None
        leftmost = root

        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            leftmost = leftmost.left
        
        return root

    # 我的solution 是传统的bfs，空间复杂度O(N) 但是题目要求O(1)， 那就要考虑到如果通过node的关系来找到下一个node， next 本来就可以用来作为桥梁
