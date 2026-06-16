class Stocks:

    def pro(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return min_price, max_profit


prices = list(map(int, input("Enter stock prices: ").split()))

obj = Stocks()

min_price, max_profit = obj.pro(prices)


print(f"Minimum price: {min_price}")
print(f"Maximum profit found: {max_profit}")