class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # My solution
        points.sort()
        res = [points[0]]

        for i in range(len(points)):
            curr = points[i]
            last = res[-1]
            if last[-1] >= curr[0]:
                res[-1] = [max(last[0],curr[0]),min(last[-1],curr[-1])]
            else:
                res.append(curr)
        return len(res)

        # My O(1) space solution
        points.sort()
        count = 1
        right = points[0][-1]
        for i in range(len(points)):
            if right < points[i][0]:
                count+=1
                right = points[i][-1]
            right = min(right,points[i][-1])
        return count

# Only need to check the boundray (right side)

# Optimal O(1) space solution
        points.sort(key= lambda x: x[-1])
        count = 1
        right = points[0][-1]
        for i in range(1,len(points)):
            if right < points[i][0]:
                count+=1
                right = points[i][-1]
        return count