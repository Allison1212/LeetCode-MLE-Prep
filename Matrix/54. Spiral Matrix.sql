class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # #My solution
        # first_row = 0
        # last_row = len(matrix) - 1

        # first_col = 0
        # last_col = len(matrix[0]) - 1

        # res = [matrix[0][0]]
        # right = left = down = up = False
        # if first_col < last_col:
        #     right = True
        # elif first_row < last_row:
        #     down = True

        # x = 0
        # y = 0
        
        # if last_row == last_col ==0:
        #     return res
        # while first_row <= last_row  and first_col <= last_col:
        #     if right:
        #         y+=1
        #         if y == last_col:
        #             right = False
        #             down = True
        #             first_row +=1
                    
        #     elif down:
        #         x+=1
        #         if x == last_row:
        #             down = False
        #             left = True
        #             last_col-=1
                    
                    
        #     elif left:
        #         y-=1
        #         if y == first_col:
        #             left = False
        #             up = True
        #             last_row-=1
                    
                    
        #     else:
        #         x-=1
        #         if x == first_row:
        #             up = False
        #             right = True
        #             first_col+=1
            
        #     res.append(matrix[x][y])
                    
        # return res
            
        res = []

        while matrix:
            res+= matrix.pop(0)

            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            
            if matrix:
                res+= matrix.pop()[::-1]
            
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
            
        return res

        # pop() 取最右
        # pop（0）取最左
        # [::-1] reverse
        # 不要只执着与一个xy点，可以看的更大一层， 宏观的数据块
        # 从“模拟物理动作”切换到“化归与降维”


        