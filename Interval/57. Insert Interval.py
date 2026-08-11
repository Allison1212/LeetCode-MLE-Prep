class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # res = []
        # insert = False
        # for i in range(len(intervals)):
        #     curr_element = intervals[i]
        #     if curr_element[0]>= newInterval[0] and not insert:
        #         res.append(newInterval)
        #         insert = True
        #     res.append(curr_element)
        # if not insert:
        #     res.append(newInterval)
        
        # sec_res = [res[0]]
        
        # for i in range(1, len(res)):
        #     curr_element = res[i]
        #     last_element = sec_res[-1]
        #     if last_element[-1]>= curr_element[0]:
        #         sec_res[-1] = [last_element[0], max(last_element[-1],curr_element[-1])]
        #     else:
        #         sec_res.append(curr_element)
        # return sec_res

        res = []
        
        for i in range(len(intervals)):
            if newInterval[-1] < intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            elif newInterval[0] > intervals[i][-1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[-1],intervals[i][-1])]
        res.append(newInterval)
        
        return res

        #还是要focus on 边的那一瞬间， 已经不变的，和之后不会变的