class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force, buy on i and then sell on all other options -> O(n2)
        # 2 ptr problem, l on day 1 and r on day 2 
        # Maximize profit -> l buy and r sell
        # If prices[l] > prices[r] -> profit negative -> update l, r by 1
        # prices[l] < prices[r] -> profit positive -> move right only as profit can go further up
        # O(n)
        l, r = 0, 1
        max_profit = 0
        # for i in range(len(prices)-1): 
        #     max_profit = max(prices[r] - prices[l], max_profit)
        #     if prices[l] > prices[r]: # Buy high, sell low
        #         l, r = l+1, r+1 # this doesnt work as l needs to go where r is (new low point)
        #     else: # Buy low, sell even higher if possible
        #         r = r +1
        while r < len(prices):
            max_profit = max(prices[r] - prices[l], max_profit)
            if prices[l] > prices[r]: # Buy high, sell low
                l = r # jump to the new minimum
            else:
                r = r + 1 
        return max_profit
