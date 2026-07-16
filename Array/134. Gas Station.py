class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # # My solution
        # if sum(gas) < sum(cost):
        #     return -1
        # else: 
        #     l = r = 0
        #     gas_sum = 0 

        #     while l <= len(gas)-1:
        #         gas_sum = gas_sum + gas[r] - cost[r]
        #         if gas[l] == 0 or gas_sum < 0:
        #             # If a point gas_sum < 0 already run out, which means the station betwen left and right are all also not work
        #             r +=1
        #             l = r 
        #             gas_sum = 0
        #         else:
        #             r = (r+1)%len(gas)
        #             if r == l:
        #                 return l
        #     return -1
        
        # Greedy solution
        # sum(gas) < sum(cost) guarantees a valid path exists.
        # The Cycle Lemma proves that if you have a sequence of numbers (like our gas/cost differences) that sum to a positive number, there is always at least one cyclic permutation (a valid starting point) where the running total never drops below zero.

        if sum(gas) < sum(cost):
            return -1
        else: 
            start = 0
            total = 0

            for i in range(len(gas)):
                total += gas[i] -cost[i]

                if total < 0:
                    start = i+1
                    total = 0
            return start
        


        