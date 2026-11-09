from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        bfs_queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if (i, j) not in visited:
                        bfs_queue.append((i, j))
                        visited.add((i, j))
                        count = 0
                        while bfs_queue:
                            curr_node = bfs_queue.popleft()
                            x, y = curr_node
                            count += 1

                            if x+1 < len(grid) and grid[x+1][y] == 1 and (x+1, y) not in visited:
                                bfs_queue.append((x+1, y))
                                visited.add((x+1, y))
                            if x-1 >= 0 and grid[x-1][y] == 1 and (x-1, y) not in visited:
                                bfs_queue.append((x-1, y))
                                visited.add((x-1, y))
                            if y+1 < len(grid[0]) and grid[x][y+1] == 1 and (x, y+1) not in visited:
                                bfs_queue.append((x, y+1))
                                visited.add((x, y+1))
                            if y-1 >= 0 and grid[x][y-1] == 1 and (x, y-1) not in visited:
                                bfs_queue.append((x, y-1))
                                visited.add((x, y-1))
                        max_area = max(max_area, count)


        return max_area