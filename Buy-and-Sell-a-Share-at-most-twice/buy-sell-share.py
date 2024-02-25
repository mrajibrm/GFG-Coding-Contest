def maxProfit(n:int, price:list[int])-> int:
    if n <= 1:
        return 0

    # dp1[i] represents the maximum profit after i-th day with at most one transaction
    dp1 = [0] * n

    # dp2[i] represents the maximum profit after i-th day with at most two transaction
    dp2 = [0] * n

    # Initialize the first Buy/Sell Operation
    min_price = price[0]
    for i in range(1, n):
        dp1[i] = max(dp1[i-1], price[i] - min_price)
        min_price = min(min_price, price[i])

    # Initialize the second Buy/Sell Operaation
    max_price = price[n-1]
    for i in range(n-2, -1, -1):
        dp2[i] = max(dp2[i+1], max_price - price[i])
        max_price = max(max_price, price[i])

    # Calculate the maximum profit by considering the combination of the two transactions
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, dp1[i] + dp2[i])

    return max_profit


def main():
    n1 = 6
    prices1 = [10,22,5,75,65,80]
    print(maxProfit(n1, prices1))

    n2 = 7
    prices2 = [2,30,15,10,8,25,80]
    print(maxProfit(n2, prices2))

if __name__ == "__main__":
    main()