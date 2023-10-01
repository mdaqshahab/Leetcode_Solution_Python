# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(self, prices: List[int]) -> int:
    s = prices[0]
    maxi = 0
    for i in prices:
        if i <= s:
            s = i
        else:
            t = i - s
            maxi = max(maxi,t)
    return maxi
