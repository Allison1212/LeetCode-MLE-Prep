class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # # My solution logic correct
        # x=0
        # str_dic = dict()

        # while x < len(board):
        #     y = 0
        #     while y < len(board):
        #         print(str_dic)
        #         char = board[x][y]
        #         if char != '.':
        #             if char in str_dic:
        #                 for last_x,last_y in str_dic[char]:
        #                     if x == last_x or y == last_y or (x//3 == last_x//3 and y//3 == last_y//3):
        #                         return False
        #                 str_dic[char].append((x,y))
        #             else:
        #                 str_dic[char] = [(x,y)]
        #         y+=1
        #     x+=1
        # return True

        # O(1 search)

        seen = set()

        for x in range(len(board)):
            for y in range(len(board)):
                char = board[x][y]

                if char != '.':
                    row = f'{char} at row {x}'
                    col = f'{char} at col {y}'
                    box = f'{char} at col {x//3} - {y//3}'
                    if row in seen or col in seen or box in seen:
                        return False

                    seen.add(row)
                    seen.add(col)
                    seen.add(box)
        return True
        # 如果不需要前后两值做计算那就不需要dict存具体index
        # 单纯的查重碰撞就用set
            

        