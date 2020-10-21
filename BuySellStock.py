def buy_sell_stock(list1):
    buyprice = float("inf")
    profit = 0
    for price in list1:
        if buyprice > price:
            buyprice = price
        else:
            profit = max(profit, price - buyprice)

    return profit
