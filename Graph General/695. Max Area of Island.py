class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:

        max_area = 0
        visit = set()
        if not grid:
            return max_area
        
        row = len(grid)
        col = len(grid[0])

        def bfs(r,c):
            directions = [[-1,0],[0,1],[1,0],[0,-1]]
            q = deque()
            q.append((r,c))
            visit.add((r,c))
            area = 1

            while q:
                r_p,c_p = q.popleft()
                for d in directions:
                    r_new = r_p + d[0]
                    c_new = c_p + d[-1]
                    if (0 <= r_new < row) and ( 0 <= c_new < col) and (grid[r_new][c_new] == 1) and ((r_new,c_new) not in visit):
                        visit.add((r_new,c_new))
                        # visit 加上了，但queue别忘了append了
                        q.append((r_new,c_new))
                        area+=1
            return area

                


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1 and ((r,c) not in visit):
                    island_area = bfs(r,c)
                    max_area = max(max_area,island_area)
        return max_area