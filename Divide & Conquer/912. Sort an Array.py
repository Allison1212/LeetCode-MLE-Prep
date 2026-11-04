class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        
        mid = len(nums) // 2

        # 这里mid 不能 left = o right = len(nums)-1, mid = left + (right-left) // 2
        # 因为当2个元素的时候，left = 0， right = 1， mid = 0， left part will be [],right = 原list 没有缩小到只
        # infinit loop

        if len(nums) <= 1:  
            return nums
        def merge(numa, numb):   
            res = []
            i = j = 0
            while i < len(numa) and j < len(numb):
                if numa[i] <= numb[j]:
                    res.append(numa[i])
                    i+=1
                else:
                    res.append(numb[j])
                    j+=1
            
            if i < len(numa):
                res = res + numa[i:]
            if j < len(numb):
                res = res + numb[j:]
            return res


        
        left_part = self.sortArray(nums[:mid])
        right_part = self.sortArray(nums[mid:])

        return merge(left_part,right_part)

        # 这题我的gap是mid边界判定 + 最小单元递归的检查（确定会缩小边界）
        # 以后要先考虑mid 的处理
        # 再确定base case
        # 再确定最后一次递归是否正确的缩小边界
        # time complexity o(nlogn)
        # space complexity o(n)
        