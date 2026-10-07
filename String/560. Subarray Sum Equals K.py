class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # 先brute force写出来，然后看怎么imrpove
        # 在一个点： current_prfix - 前部分的prefix = k
        # 想到只要找到前面 能组成current_prefix - k 的substring 有几个就行
        # 这样就想到存prefix 的count，当前面能成立的时候直接拿出来+ final count 就好
        # 一个substring只有一个ending position，所以只要end不一样就是全新substring 所以不会重复累加
        from collections import defaultdict
        prefix_map = defaultdict(lambda: 0)
        prefix_map[0] = 1

        prefix = 0
        res = 0

        for n in nums:
            prefix+=n
            if (prefix-k) in prefix_map:
                res+= prefix_map[prefix-k]
            
            prefix_map[prefix] = prefix_map[prefix]+1
        return res