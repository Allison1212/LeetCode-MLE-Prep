class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # # Brute force: Time complexity O(nlogn); Space complexity O(n)
        # nums_count = {}

        # for n in nums:
        #     if n not in nums_count:
        #         nums_count[n] = 1
        #     else:
        #         nums_count[n] = nums_count[n] + 1
        
        # sort_dict = dict(sorted(nums_count.items(), key = lambda x: x[1], reverse = True))

        # return list(sort_dict.keys())[:k]


        # Bucket sort
        nums_count = {}
        res = []
        # frequncy arrary, index是frequncy， list 是value 他是这个frequency
        freq = [[] for _ in range(len(nums)+1)]
        # 不能freq = [[]] * (len(nums) + 1)， 因为这inner list 指向一个memory 所有会出现append 一个index每个list 都update 了
        # 第一步总还是要get count dict 的
        for n in nums:
            nums_count[n] = 1 + nums_count.get(n,0)
        
        # create frequncy arrary
        for n, c in nums_count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0 , -1):
            # 如果freq[i]是空会直接跳过
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res