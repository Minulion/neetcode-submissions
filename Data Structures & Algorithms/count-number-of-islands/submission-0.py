class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        from collections import deque

        visited = set() # set of tuples, (row, col)
        num_islands = 0
        height = len(grid) # num rows
        width = len(grid[0]) # num cols

        # start bfs to find nodes that are part of islands
        # only start if node == "1" and not visited

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # check neighbors by adding from this array

        # iterate thru all nodes
        for row_num, row in enumerate(grid):
            for col_num, node_val in enumerate(row):

                # filter out invalid start nodes
                if (row_num, col_num) in visited or node_val == "0":
                    continue

                # init bfs with start node
                queue = deque([(row_num, col_num)])
                visited.add((row_num, col_num))

                while queue:
                    r, c = queue.popleft() # row and col num of start node

                    # add x and y of each direction, add to island if needed
                    for dr, dc in directions:
                        if 0 <= r + dr < height and 0 <= c + dc < width:
                            if grid[r + dr][c + dc] == "1" and (r + dr, c + dc) not in visited:
                                queue.append((r + dr, c + dc))
                                visited.add((r + dr, c + dc))

                num_islands += 1
                
        return num_islands