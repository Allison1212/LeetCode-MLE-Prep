class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # # sort a list of list it will automatically sort based on first value
        # intervals.sort()
        # res = [intervals[0]]
        # for i in range(1,len(intervals)):
        #     last_value = res.pop()
        #     if last_value[-1] >= intervals[i][0] and last_value[-1] <= intervals[i][-1]:
        #         res.append([last_value[0],intervals[i][-1]])
        #     else:
        #          res.append(last_value)
        #          if last_value[-1] < intervals[i][0]:
        #             res.append(intervals[i])
        # return res
        intervals.sort()
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            last_element = res[-1]
            current_element = intervals[i]
            if last_element[-1] >= current_element[0]: 
                res[-1] = [last_element[0],max(last_element[-1],current_element[-1])]
            else:
                res.append(intervals[i])
        return res

    #只要瞄准特殊情况，要做处理的part