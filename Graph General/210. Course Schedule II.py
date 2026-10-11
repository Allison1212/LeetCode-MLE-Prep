class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        res = []
        visited = set()
        
        pre_crs_map = { crs: [] for crs in range(numCourses) }

        for crs, pre in prerequisites:
            pre_crs_map[crs].append(pre)
        
        def dfs(crs,path):
            if crs in path:
                return False
            if crs in visited:
                return True

            path.add(crs)
            pre_lst = pre_crs_map[crs]
            
            for pre in pre_lst:
                if not dfs(pre,path): return False

            path.remove(crs)
            res.append(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
           if not dfs(crs,set()): return []
        
        return res

        # 这里我的gap 没有马上意识到需要一个独立的状态来记录 DFS 已经完成的节点 -- set。 course schedule 1 的meet requirment 是 pre list is empty
        # 但这里用visit set 也可以达到
        # time complexity O(V + N)
        # Space O(V + N)