class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def bfs(r,c):
            directions = [[-1,0],[0,1],[1,0],[0,-1]]
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                r_new, c_new = q.popleft()
                for d in directions:
                    r_d = r_new+d[0]
                    c_d = c_new+d[-1]
                    if ((0<= r_d < row) and (0<= c_d < col) and grid[r_d][c_d] == '1' and ((r_d, c_d) not in visit)):
                        q.append((r_d,c_d))
                        visit.add((r_d, c_d))
                        
        count = 0
        if not grid:
            return count
        
        visit = set()

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c]  == "1" and ((r,c) not in visit):
                    bfs(r,c)
                    count += 1
        
        return count


        # 这里有几个要点：
        # 逻辑没有问题 是bfs + meet 条件count +=1， 但是一开始这个条件想不明白，这里其实就是大局观，先写主框架，见到“1” 的时候要干什么
        # 这里想不到的原因是没想清楚做一次bfs 的前后变化， 变化前是一个单独的“1” point 没有visited， 变化后和这个“1”相连的point 都被visited
        # 这样但凡有一个新的1 没有被visited 就是一个新的island

        # 然后关于bfs algorithm， 
        # bfs 用q 以最先接触的点往外， dfs 用stack 以最后一个点一直往一个方向
        # 这里注意坐标variable，明确原坐标和新坐标
        # 要搜索的范围有， 1. 新坐标是不是在范围内 2.新坐标有没有被visited 3. 根据题的指示划定边界，比如到什么就停
        # 看到一个新坐标的时候就直接加入列队， 不然如果一个格子被反复看见，但因为他还没pop就没被加进去，就会多次被加入queue
        