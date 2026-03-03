# My Solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)*2

        for i in range(0,len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]

        return ans
    
# Better Solution 1
# python 的列表连接操作符 + 和乘法操作符 * 都是非常高效的，因为它们在底层使用了 C 语言实现的优化算法来处理内存分配和数据复制。因此，直接使用 nums + nums 或 nums * 2 是一种非常简洁且高效的方式来实现数组的连接。
# nums + nums 是两个list合并， numpy 的 + 是vectorized的加法运算， 这里的 + 是 list 的连接操作符
# time complexity: O(n) 因为需要遍历一次 nums 来创建新的列表 和我的解法一样， 但是底层实现更高效
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 这种写法直接利用了 Python 的内置优化
        return nums + nums
        # 或者 return nums * 2


        
# Better Solution 2
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums.extend(nums)
        return nums