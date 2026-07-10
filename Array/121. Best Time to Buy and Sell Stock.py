class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Solution 1: 
        # adopt a pattern called "Reactive Updating." Instead of trying to maintain the "current max state," just react to the current price.
        max_profit = 0
        min_price = float('inf')

        for sell in range(0,len(prices)):
            min_price = min(prices[sell],min_price)
            max_profit = max(max_profit, prices[sell] - min_price)

        return max_profit

       

        # My Solution:
        min_price = max_price = prices[0]
        best_gain = max_price - min_price
        for i in range(1,len(prices)):
            print(min_price,max_price)
            if prices[i] <= min_price:
                min_price = max_price = prices[i]
                
            else:
                max_price = max(prices[i],max_price)
            
            best_gain = max(best_gain,max_price - min_price)

        return best_gain