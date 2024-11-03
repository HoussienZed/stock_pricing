# defining a function to calculate max profit

def max_profit(prices):
    # adding initial values for variables
    buying_day = 0
    selling_day = 1
    highest_profit = prices[1] - prices[0]
    for i in range(len(prices)):
        for j in range(len(prices)):
            if i >= j:  # we cannot buy and sell on same day or on a day before
                continue
            if prices[j] - prices[i] > highest_profit:
                buying_day = i + 1
                selling_day = j + 1
                highest_profit = prices[j] - prices[i]

    return (print(f"The best days to buy and sell are day {buying_day}, and day {selling_day}, where the max profit is {highest_profit}"))


# entering the prices on different days

days_num = int(input("For how many days do you want to check your profit: "))
daily_prices = []
for i in range(days_num):
    price = int(input(f"Enter the price on day {i + 1}: "))
    daily_prices.append(price)


max_profit(daily_prices)
