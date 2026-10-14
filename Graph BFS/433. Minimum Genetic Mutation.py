class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        visited = set()
        queue = deque()
        queue.append([startGene,0])
        visited.add(startGene)

        while queue:
            q,moves = queue.popleft()
            for g in bank:
                if g not in visited:
                    # diff = 0
                    # for c,b in zip(q,g):
                    #     if c!=b:
                    #         diff+=1
                    diff = sum(c != b for c, b in zip(q, g))
                    if diff == 1:
                        if g == endGene:
                            return moves+1
                        queue.append([g,moves+1])
                        visited.add(g)
        return -1

        # time complexity O(8n^2)
        # Space complexity O(n)

        # 想到了adjacent map -> for loop count to find 1 mutation -> BFS shortest path (gap)
        # my problem: stop before the BFS, because I think adjacent map and for loop already complicated and don't think that is right route. 