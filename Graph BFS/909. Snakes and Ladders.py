class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        
        length = len(board)

        # Reverse the board, nothing will change 
        board.reverse()
        # Help function to get the r, c for each point
        def intToPos(point):
            r = (point-1) // length
            c = (point-1) % length

            if r % 2:
                c = length - 1 - c

            return [r,c]

        # BFS for each point, and use visited set to skip visited point 

        visited = set()

        queue = deque() # [point,moves]

        queue.append([1,0])
        visited.add(1)

        while queue:
            point,moves = queue.popleft()

            for i in range(1,7):
                new_point = point + i
                # Out of index check
                if new_point > length * length:
                    break
                # if snakes or ladders
                r,c = intToPos(new_point)
                if board[r][c] != -1:
                    new_point = board[r][c]
                # if the point is n^2 return the result
                if new_point == length * length:
                    return moves + 1
                # Add to queue if not visited
                if new_point not in visited:
                    # Don't forget to add new point to visited
                    visited.add(new_point)
                    queue.append([new_point,moves + 1])
        
        return -1
        # Time complexity O(n^2)
            #n = 棋盘边长，那么复杂度是 O(n²)， V = 棋盘格子总数，那么复杂度是 O(V)。
        # Space complexity O(n^2)
