class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        prere_dict = {crs:[] for crs in range(numCourses)}

        for crs, pre in prerequisites:
            prere_dict[crs].append(pre)

        
        def dfs (crs,path):
            if crs in path:
                return False
            if prere_dict[crs] == []:
                return True

            path.add(crs)
            for p in prere_dict[crs]:
                if not dfs(p,path): return False

            path.remove(crs)
            prere_dict[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs,set()): return False
        
        return True

        # Time complexity O(N+P)
        # Space complexity O(N+p)

        # 这题要点是首先要先会create adjcency list
        # 然后dfs 走遍所有path， 如果有cycle 就false （这个用set我想到了
        # 但是 【】return true 没想到