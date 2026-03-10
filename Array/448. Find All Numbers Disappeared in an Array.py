class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # out = list()
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         out.append(i)

        # Time Complexity: O(n log n) due to the sorting step
        # Space Complexity: O(n) for storing the sets and lists
        range_lst = [i for i in range(1,len(nums)+1)]
        out = list(set(range_lst) - set(nums))
        out.sort()
        return out
    

# Less space complexity solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for n in nums:
            if nums[abs(n)-1] > 0:
                nums[abs(n)-1] = - nums[abs(n)-1]
        
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
