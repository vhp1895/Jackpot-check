#!/usr/bin/env python3

import argparse
from requests_html import HTMLSession


'''
    The script checks if your coupons match loto prize.
    Otherwise, print special prize to 7th-place prize

    To check ticket:
    python3 ketqua.py [Number1] [Number2] ... -check

    To print all prize:
    python3 ketqua.py
'''


def loto_check(coupon_list):

    session = HTMLSession()
    r = session.get('http://ketqua.net')
    sel = '#loto_mb > tbody > tr > td'

    feel_good = []

    jackpot_list = []

    for i in range(len(r.html.find(sel))):
        jackpot_list.append(r.html.find(sel)[i].text)

    for coupon in coupon_list:
        if coupon in jackpot_list:
            feel_good.append(coupon)

    return feel_good


def traditional_lottery(arg=None):

    session = HTMLSession()
    r = session.get('http://ketqua.net')
    sel = '#result_tab_mb > tbody > tr > td'

    jackpot = {}

    for element in r.html.find(sel):
        if element.text:
            if not element.text.isdigit():
                current_prize = element.text
                jackpot[current_prize] = []
            else:
                jackpot[current_prize].append(element.text)

    return jackpot


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('lottery_coupon', type=str, nargs='*')
    parser.add_argument('-check', action='store_const',
                        const=loto_check, default=traditional_lottery)

    args = parser.parse_args()
    print(args.check(args.lottery_coupon))


if __name__ == '__main__':
    main()
