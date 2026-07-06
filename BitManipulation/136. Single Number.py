class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # new_lst = list()

        # for i in nums:
        #     if i in new_lst:
        #         new_lst.remove(i)
        #     else:
        #         new_lst.append(i)
        # return new_lst[0]


        # XOR 
        # Us XOR property:
        # Same numbers XOR to zero: Formula: a ^ a = 0
        # XOR with zero returns original Formula: a ^ 0 = a
        # Commutative Formula: a ^ b = b ^ a
        # Associative Formula: (a ^ b) ^ c = a ^ (b ^ c)
        res = 0

        for i in nums:
            res ^= i
        return res

