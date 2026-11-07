class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = 101
        minimum_prices = []
        for i in prices:
            if i < minimum_price:
                minimum_price = i
            minimum_prices.append(minimum_price)

        profits = [prices[i] - minimum_prices[i] for i in range(len(prices))]

        return max(profits)