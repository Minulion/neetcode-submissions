"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        cloned = {} # maps og node to clone

        def dfs(node): # returns copy of graph using dfs

            # if already cloned, return from dict
            if node in cloned:
                return cloned[node]
            
            # clone node and put into dict
            clone = Node(node.val)
            cloned[node] = clone

            # populate clone neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
                
        return dfs(node)

        