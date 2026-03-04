class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = []
        i = 0
        j = i + n

        while i < n:
            out.append(nums[i])
            out.append(nums[j])
            i = i + 1
            j = j + 1
        return out 

    # Time Complexity: O(n) – we traverse the list once, performing
    # a constant amount of work per element.
    # Space Complexity: O(n) – we create an output list of size 2n
    # (which is linear in the size of the input).