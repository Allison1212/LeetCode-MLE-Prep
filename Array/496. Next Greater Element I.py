class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # out_list = []

        # for n in nums1:
            
        #     i = 0
        #     find = False
        #     while i < len(nums2):
        #         print(n,i,out_list)
        #         if nums2[i] == n:
        #             find = True
        #             i = i + 1
        #         else:
        #             if find:
        #                 if max(nums2[i:]) < n:
        #                     out_list.append(-1)
        #                     break
        #                 if nums2[i] > n:
        #                     out_list.append(nums2[i])
        #                     break
        #             i = i + 1
        #     if i > len(nums2) -1:
        #         out_list.append(-1)

        # return out_list

        # Use a monotonic decreasing stack to find the next greater element for each element in nums2, and use a hash map to map to nums1 index. 
        res = [-1] * len(nums1)
        
        idx_map = {}
        for i, n in enumerate(nums1):
            idx_map[n] = i

        print(idx_map)

        stack = []
        
        i = 0
        for i in nums2:
            print(i)
            while stack and (i > stack[-1]):
                val = stack.pop()
                if val in idx_map.keys():
                    idx = idx_map[val]
                    res[idx] = i
            stack.append(i)
        return res