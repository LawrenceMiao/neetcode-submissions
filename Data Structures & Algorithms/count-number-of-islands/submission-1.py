from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited: set[tuple[int, int]] = set()
        count = 0

        bfs_queue = deque([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    if (i, j) not in visited:
                        count += 1
                        bfs_queue.append((i, j))
                        visited.add((i, j))
                        while bfs_queue:
                            x, y = bfs_queue.popleft()
                            if x+1 < len(grid) and grid[x+1][y] == "1" and (x+1, y) not in visited:
                                bfs_queue.append((x+1, y))
                                visited.add((x+1, y))
                            if x-1 >= 0 and grid[x-1][y] == "1" and (x-1, y) not in visited:
                                bfs_queue.append((x-1, y))
                                visited.add((x-1, y))
                            if y+1 < len(grid[0]) and grid[x][y+1] == "1" and (x, y+1) not in visited:
                                bfs_queue.append((x, y+1))
                                visited.add((x, y+1))
                            if y-1 >= 0 and grid[x][y-1] == "1" and (x, y-1) not in visited:
                                bfs_queue.append((x, y-1))
                                visited.add((x, y-1))

        return count