"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        # Global variable
        oldToNew = {}
        # What is input and what is output: input (node), out (copy of node)

        def clone(node):
            # If this node copy has been created, how to check? -> a place to store
            if node in oldToNew:
                return oldToNew[node]
            # If node has not been copyed 
            # Create node, first it's value -> neighbors
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            
            return copy

        return clone(node)