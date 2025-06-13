from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Human Thinking Steps:

        1. Scan each cell of the grid
           → Use grid[r][c] to access each cell

        2. If I find '1', it means a new island
           → Increment the island counter
           → Initialize islands = 0

        3. Start a DFS from that cell to “sink” the island
           → Define a DFS function
           → Sink current land by marking grid[r][c] = "0"
           → Recursively sink connected lands: dfs(r+dr, c+dc)
           → Define directions for adjacent land (up, down, left, right)
           → Avoid out-of-bound indices or water ('0')

        4. Continue scanning the grid

        5. Return the total island count after the full scan
        '''

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]  # down, up, right, left

        def dfs(r, c):
            # Base case: if out of bounds or already water, stop recursion
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            # Mark current land as visited by sinking it
            grid[r][c] = "0"
            # Recursively visit all 4 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # Found new island
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)  # Sink the entire island

        return islands
