class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        node_dict = collections.defaultdict(list)

        # 不要想着见到一个node 就算好他和所有node 的关系然后同时update
        # 把数学原理转化为graph
        for i, eq in enumerate(equations):
            num,den = eq
            node_dict[num].append([den,values[i]])
            node_dict[den].append([num,1/values[i]])
        
        # Chain a/b * b/c = a/c = v1*v2
        def bfs (start, end):
            query,visited = deque(),set()
            query.append([start,1])
            visited.add(start)

            while query:
                n,v = query.popleft()
                if n == end:
                    return v
                for nei in node_dict[n]:
                    nei_n,nei_v = nei[0], nei[1]

                    if nei_n not in visited:
                        v_new = v * nei_v
                        query.append([nei_n,v_new])
                        visited.add(nei_n)
            # 存在连不成一个chain/graph 的，就是start的往外搜索完没到end，那要return -1
            return -1
        return  [bfs(q[0], q[1]) if (q[0] in node_dict) and (q[1] in node_dict) else -1 for q in queries]
        #时间复杂度：O(M/N)
        # 空间复杂度：O(N)
