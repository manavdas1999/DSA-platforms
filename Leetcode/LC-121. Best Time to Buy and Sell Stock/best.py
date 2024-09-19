
# Time: O(n), space: O(1)


def maximumProfit(self, prices):
        maxProfit = 0
        # started by the thought the minimum buying price is at 1st day
        minBuyPrice = prices[0]
        # going through each price looking for a better buying day(lesser buy day)
        # and also calculating the profit for current selected buying day
        for p in prices:
            minBuyPrice = min(minBuyPrice, p)
            maxProfit = max(maxProfit, p - minBuyPrice)
                
        return maxProfit
