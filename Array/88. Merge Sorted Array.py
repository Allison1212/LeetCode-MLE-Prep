class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = m-1
        j = n-1
        p = m+n-1

        while i >=0 and j >=0:
            if nums1[i]>= nums2[j]:
                nums1[p] = nums1[i]
                i-=1
            else:
                nums1[p] = nums2[j]
                j-=1
            p-=1
        
        if j>=0:
            nums1[:j+1] = nums2[:j+1]

    # Identified the overwrite issue when merging left to right.
    # Tried moving overwritten elements to the end, but couldn't maintain sorted order.
    # Gap: Didn't realize merging right to left avoids overwriting entirely (I only think about sort in one direction).
    # Key Takeaway
    # - When overwriting occurs, consider reversing the traversal direction instead of moving or storing elements.
    

    # Time complexity = O(m+n)
    # Space complexity = O(n)
