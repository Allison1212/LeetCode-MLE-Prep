# My solution:
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) < 4:
            return False
        else:
            if nums[1] <= nums[0]:
                return False
            else: 
                idx = 1
                p = list()
                q = list()
                while idx < len(nums)-1:
                    if nums[idx -1] == nums[idx] or nums[idx  + 1] == nums[idx]:
                        return False
                    if (nums[idx -1] < nums[idx]) and (nums[idx] > nums[idx + 1]):
                        p.append(idx)
                    if (nums[idx -1] > nums[idx]) and (nums[idx] < nums[idx + 1]):
                        print(idx)
                        q.append(idx)
                    idx = idx + 1
                    print (p,q)
                return (len(p) == len(q) == 1) and  (q[0] > p[0] != 0)



    # Time Complexity: O(n) – we traverse the list once, performing
    # a constant amount of work per element.
    # Space Complexity: O(n) – we create two additional lists `p`
    # and `q` that can grow up to size n in the worst case (when

# Better solution: search peak and valley from left to right, and check if there is only one peak and one valley, and the valley is after the peak.
class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        # A trionic array has exactly 3 phases:
        # 1. Strictly increasing (at least 2 elements)
        # 2. Strictly decreasing (at least 2 elements)
        # 3. Strictly increasing (at least 2 elements)
        
        n = len(nums)
        if n < 4: 
            return False
        
        i = 0
        
        # Phase 1: Strictly increasing
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        
        # Need at least 2 elements before peak
        if i < 1:
            return False
        
        # Phase 2: Strictly decreasing
        peak = i
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1
        
        # Need at least 2 elements in decreasing phase
        if i < peak + 1:
            return False
        
        # Phase 3: Strictly increasing
        valley = i
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1
        
        # Need at least 2 elements in final increasing phase
        if i < valley + 1:
            return False
        
        # Must consume entire array
        return i == n - 1
    
    # Time Complexity: O(n) – single pass through the array.
    # Space Complexity: O(1) – only using a constant amount of extra space.