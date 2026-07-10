lass Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # My first draft
        # res = 0
        
        # left = last_r = 0
        # right = 1
        # if len(prices) <=1:
        #     return res
        # else:

        #     while right <=len(prices) -1:
                
        #         if prices[left] > prices[right]:
        #             left = right
        #             right+=1
        #             last_r = left
        #         else:
        #             if prices[right] > prices[last_r]:
        #                 res = res + (prices[right]-prices[last_r])
        #                 last_r = right 
        #                 right +=1
        #             else:
        #                 left = last_r = right 
        #                 right += 1
        #     return res
        
        # My simplified solution: finding ascending part
        res = 0
        last_r = 0
        right = 1
        if len(prices) <=1:
            return res
        else:
            while right <=len(prices) -1:
                if prices[last_r] <= prices[right]:
                    if prices[right] > prices[last_r]:
                        res += (prices[right]-prices[last_r])
                last_r = right 
                right += 1
            return res
        
        # Optimal solution: 
        # By first day sell third day is equal to buy first day sell second and but second sell thrid
        # Finding the acending subpart and add together 

        res = 0
        for i in range (1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        
        return res
                

        