#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # set the first price to be the initial buy price
    buy_price = prices[0]
    # initialize max so far
    max_profit_so_far = 0

    for i in range(len(prices) - 1):
        # check profit or loss -> profloss
        profit = prices[i + 1] - buy_price
        if profit > max_profit_so_far or (max_profit_so_far == 0 and profit < 0):
            max_profit_so_far = profit
        # if the stocks have fallen, buy another one
        if prices[i + 1] < buy_price:
            buy_price = prices[i + 1]
    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
