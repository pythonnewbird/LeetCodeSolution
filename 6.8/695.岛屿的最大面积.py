class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    ans = max(ans, self.bfs(grid, x, y))
        return ans
    def bfs(self, grid, x, y):
        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]
        queue = [(x, y)]
        grid[x][y] = 0
        ans = 0
        while queue:
            x, y = queue.pop(0)
            ans += 1
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    if grid[nx][ny]:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
        return ans