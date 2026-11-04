"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        if not grid:
            return None
        new_node = Node(None, None, None, None, None, None)
        rows = len(grid)
        cols = len(grid[0])
        row_mid = rows//2
        col_mid = cols//2

        # if grid[0][0] == grid[0][-1] == grid[-1][0] == grid[-1][-1]:
        # 比四个角不够，要每个cell 都比过去
        if all(cell == grid[0][0] for row in grid for cell in row):
            new_node.isLeaf = True
            new_node.topLeft = None
            new_node.topRight = None
            new_node.bottomLeft = None
            new_node.bottomRight = None

            if grid[0][0] == 1:
                new_node.val = True
            else:
                new_node.val = False
        else:
            new_node.isLeaf = False
            new_node.val = True

            # 思路是对的， 但二维的slicing 不是这么写的
            # new_node.topLeft = help(grid[:row_mid][:col_mid])
            # new_node.topRight =  help(grid[:row_mid][col_mid:])
            # new_node.bottomLeft = help(grid[row_mid:][:col_mid])
            # new_node.bottomRight = help(grid[row_mid:][col_mid:])

            new_node.topLeft = self.construct([row[:col_mid] for row in grid[:row_mid]])
            new_node.topRight = self.construct([row[col_mid:] for row in grid[:row_mid]])
            new_node.bottomLeft = self.construct([row[:col_mid] for row in grid[row_mid:]])
            new_node.bottomRight = self.construct([row[col_mid:] for row in grid[row_mid:]])

        return new_node
        # 这里我只要return node 就行了，题目要求返回的是 QuadTree 的 root node

        # Time complexity: O(n2logn)
        # Space complexity: O(n^2)
        # Recursion stack: (O(log n))，因为每次边长减半。
        #Grid slicing: (O(n^2))，递归过程中会创建新的二维数组。
        #QuadTree nodes: 最坏情况下 (O(n^2)) 个节点。
