class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        # use max heap to keep track of the most frequent tasks
        # use a queue to keep track of tasks that are on cooldown
        fre_dict = {}

        for t in tasks:
            if t not in fre_dict:
                fre_dict[t] = 1
            else:
                fre_dict[t] +=1
        
        max_heap = [-cnt for cnt in fre_dict.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0

        while max_heap or q:
            time+=1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time+n])
            if q and q[0][-1] == time:
                heapq.heappush(max_heap,q.popleft()[0])
        return time
        # T total task, U unique tasks, L total time
        # Time complexity 
        # each task is processed once and heap operations take O(logU) -> T task * O(logU) = O(TlogU)
        # Since there is also idle time, the actual time complexity could be O(TlogU + L) 
        # Space complexity O(U)




        return time
