class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_area = 0

        # for i in range(len(height)):
        #     right = i + 1
        #     if right + 1 < len(height) and min(height[right],height[right + 1]) > min(height[i],height[right + 1]) * 2:
        #         continue
        #     while right < len(height):
        #         wide = right - i
        #         hight = min(height[i],height[right])
        #         max_area = max(max_area,wide*hight)
        #         right += 1
        # return max_area

        max_area = 0

        left = 0
        right = len(height) -1

        while left < right:
            wide = right - left 
            high = min(height[left],height[right])

            max_area = max(max_area, wide*high)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        
        return max_area

        # 有的时候学会做减法instead of 做加法，two pointer可以在两端