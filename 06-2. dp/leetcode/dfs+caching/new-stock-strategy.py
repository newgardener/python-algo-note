def calculate_profit(rates, strategy):
    profit = 0
    buy_price = None
    max_sell_price = 0

    for i, (rate, action) in enumerate(zip(rates, strategy)):
        # Buy
        if action == -1:
            if buy_price is not None and max_sell_price > buy_price:
                profit += max_sell_price - buy_price
            buy_price = rate
            max_sell_price = 0
        # Sell
        elif action == 1 and buy_price is not None:
            max_sell_price = max(max_sell_price, rate)

        if i == len(rates) - 1 and buy_price is not None:
            profit += max(max_sell_price, rate) - buy_price
    return profit


def apply_new_strategy(rates, start, k, buy_price):
    if buy_price is None:
        return 0
    sell_price = max(rates[start + k // 2 : start + k])
    return max(0, sell_price - buy_price)


def max_profit_with_new_strategy(rates, strategy, k):
    n = len(rates)
    original_profit = calculate_profit(rates, strategy)
    max_profit = original_profit

    for start in range(n - k + 1):
        # Calculate profit and buy price before new strategy
        profit_before = 0
        buy_price = None
        max_sell_price = 0
        for i in range(start):
            # Buy
            if strategy[i] == -1:
                if buy_price is not None and max_sell_price > buy_price:
                    profit_before += max_sell_price - buy_price
                buy_price = rates[i]
                max_sell_price = 0
            # Sell
            elif strategy[i] == 1 and buy_price is not None:
                max_sell_price = max(max_sell_price, rates[i])

        # Apply new strategy
        new_strategy_profit = apply_new_strategy(rates, start, k, buy_price)

        # Calculate profit after new strategy
        profit_after = calculate_profit(rates[start + k :], strategy[start + k :])

        # Total profit
        total_profit = profit_before + new_strategy_profit + profit_after

        max_profit = max(max_profit, total_profit)

    return max_profit


# Example
strategy = [-1, 1, 0, 1, -1, 0]
rates = [2, 4, 1, 5, 10, 6]
k = 4
result = max_profit_with_new_strategy(rates, strategy, k)
print(f"Maximum Profit: {result}")
