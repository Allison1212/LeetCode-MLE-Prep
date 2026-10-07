class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # brute force
        # res = len(temperatures) * [0]
        # for i in range(len(temperatures)):
        #     count = 0
        #     right = i + 1
        #     while right < len(temperatures):
        #         count+=1
        #         if temperatures[right] > temperatures[i]:
        #             res[i] = count
        #             break
        #         right+=1
        # return res
        
        # monotonic decreasing stack
        stack = list()
        res = len(temperatures) * [0]

        # 这里不用单独if 判断了，直接用while stack， 然后check 是否空先，这样如果自动空就会skip到下面的判断
        # 每新的value 进来只要和stack的最后一位判断就好
        for i, v in enumerate(temperatures):
            while stack and stack[-1][-1] < v:
                res[stack[-1][0]] = i-stack[-1][0]
                stack.pop()
            stack.append([i,v])

        return res
        # time complexity O(N)
        # Space complexity O(N)