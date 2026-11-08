class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        from collections import defaultdict

        adj_list = defaultdict(list)
        for edge in edges:
            a, b = edge
            adj_list[a].append(b)
            adj_list[b].append(a)

        mapped = set()
        components = 0

        #adjacency list assembled, now dfs to find all paths
        #approach: dfs from node, add connected nodes to set of "visited"
        #each time a node is not in visited, you have a new component
        #for each new component run dfs
        #runtime: dfs x #components

        for i in range(n):
            if i not in mapped:
                components += 1
                self.dfs(i, adj_list, mapped)

        return components
    
    def dfs(self, n, adj_list, mapped):
        mapped.add(n)

        for i in adj_list[n]:
            if i not in mapped:
                self.dfs(i, adj_list, mapped)
        return




