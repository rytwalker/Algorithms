#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # first pass solution
    # We have to init buy first price
    # if there is a lower price we can only buy that one
    # if there is a bigger sell point after

    buy = prices[0]
    sell = prices[1]

    for price in prices:
        if price > buy:
            sell = price

    for price in prices:
        if price == sell:
            break
        if price < buy:
            buy = price

    print(f"sell: {sell}, buy: {buy}")

    max_profit = sell - buy

    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
