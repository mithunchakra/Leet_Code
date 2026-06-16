class Stock2:

    def maxProfit(self, prices):

        profit = 0

        for i in range(1, len(prices)):

            if prices[i] > prices[i - 1]:

                profit += prices[i] - prices[i - 1]

        return profit


prices = list(map(int, input("Enter prices: ").split()))

obj = Stock2()

print("Maximum Profit:", obj.maxProfit(prices))